from motor.motor_asyncio import AsyncIOMotorClient
import os

mongo_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(mongo_URI)
db = client.analytics