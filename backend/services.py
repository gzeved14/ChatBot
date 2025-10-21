# services.py
from backend.chatbot.nlp import AdvancedNLP
from dotenv import load_dotenv
import os
from openai import OpenAI
from pathlib import Path
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam

# ------------------------------
# Carregar variáveis do .env
# ------------------------------
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENAI_API_KEY")
print("Chave carregada:", API_KEY)  # Confirma que está carregando corretamente

# Inicializar cliente OpenAI
client = OpenAI(api_key=API_KEY)

# Inicializar NLP customizado
nlp = AdvancedNLP()

# ------------------------------
# Função principal do chatbot
# ------------------------------
def process_message(user_message: str) -> str:
    """
    Primeiro tenta responder com NLP baseado em intents.
    Se não houver resposta, usa ChatGPT como fallback.
    """
    # 1️⃣ Tenta responder com base nos intents
    nlp_response = nlp.find_intent_and_response(user_message)
    if nlp_response:
        return nlp_response

    # 2️⃣ Se não houver resposta baseada em intents, usa ChatGPT
    try:
        messages: list[ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam] = [
            ChatCompletionSystemMessageParam(content="Você é um assistente educado, objetivo e útil."),
            ChatCompletionUserMessageParam(content=user_message)
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # ou gpt-3.5-turbo, dependendo do seu plano
            messages=messages
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Erro ao chamar ChatGPT:", e)
        return "Desculpe, não consegui entender sua pergunta."
