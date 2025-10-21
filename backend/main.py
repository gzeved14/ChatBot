# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager

from db import connect_to_mongo, close_mongo_connection, get_database
from chatbot.nlp import AdvancedNLP

# Inicializa NLP
nlp = AdvancedNLP()

# Modelo de request
class ChatRequest(BaseModel):
    user_id: str
    message: str

# Funções para mensagens no MongoDB
async def save_message(user_id: str, user_text: str, bot_response: str):
    db = get_database()
    if not db:
        raise HTTPException(status_code=500, detail="MongoDB não conectado")
    messages_col = db["messages"]
    await messages_col.insert_one({
        "user_id": user_id,
        "user_text": user_text,
        "bot_response": bot_response
    })

async def get_history(user_id: str):
    db = get_database()
    if not db:
        raise HTTPException(status_code=500, detail="MongoDB não conectado")
    messages_col = db["messages"]
    cursor = messages_col.find({"user_id": user_id})
    history = []
    async for doc in cursor:
        history.append({
            "user_text": doc["user_text"],
            "bot_response": doc["bot_response"]
        })
    return history

# Lifespan handler para startup e shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()   # startup
    yield
    await close_mongo_connection()  # shutdown

# Cria app com lifespan
app = FastAPI(title="ChatBot API", lifespan=lifespan)

# Endpoint para enviar mensagem
@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    user_message = chat_request.message
    user_id = chat_request.user_id

    # Processa mensagem com NLP + OpenAI
    response = nlp.find_intent_and_response(user_message)

    # Salva interação no MongoDB
    await save_message(user_id, user_message, response)

    return {"response": response}

# Endpoint para histórico
@app.get("/history/{user_id}")
async def history_endpoint(user_id: str):
    return await get_history(user_id)

# Para rodar: uvicorn main:app --reload
