import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# URL de conexão com o MongoDB
MONGO_DETAILS = os.getenv(
    "MONGO_DETAILS",
    "mongodb+srv://gzeved:Azeved0%211@cluster0.ogdkgpa.mongodb.net/chatbot_db?retryWrites=true&w=majority"
)

# Cliente do MongoDB
client: AsyncIOMotorClient | None = None

# Conectar ao MongoDB
async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(MONGO_DETAILS)
    print("Conexão com o MongoDB estabelecida com sucesso!")

# Fechar conexão
async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("Conexão com o MongoDB fechada.")

# ✅ Função para pegar o banco de dados
def get_database():
    if client:
        return client["chatbot_db"]
    else:
        raise Exception("MongoDB não conectado. Execute connect_to_mongo() antes.")
