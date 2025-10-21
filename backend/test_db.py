import asyncio
from db import connect_to_mongo, close_mongo_connection, get_database

async def test_connection():
    await connect_to_mongo()
    db = get_database()
    print("Database:", db)
    await close_mongo_connection()

asyncio.run(test_connection())
