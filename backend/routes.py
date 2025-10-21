# routes.py
from fastapi import APIRouter
from pydantic import BaseModel
from backend.services import process_message

router = APIRouter()

# Modelo de dados para a mensagem recebida
class Message(BaseModel):
    message: str

# Endpoint principal do chat
@router.post("/chat")
async def chat_endpoint(msg: Message):
    """
    Recebe a mensagem do usuário e retorna a resposta do chatbot.
    """
    user_message = msg.message
    chatbot_response = process_message(user_message)
    return {"response": chatbot_response}
