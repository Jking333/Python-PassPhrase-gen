import motor.motor_asyncio
from model import Results

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.PhraseList
collection = database.phrase

async def fetch_one_phrase(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_phrases():
    phrases = []
    cursor = collection.find({})
    async for document in cursor:
        phrases.append(Results(**document))
    return phrases

async def create_phrase(phrase):
    document = phrase 
    result = await collection.insert_one(document)
    return document

async def update_phrase(title, word):
    await collection.update_one({"title": title}, {"$set": {"word": word}})
    document = await collection.find_one({"title": title})
    return document

async def remove_phrase(title):
    await collection.delete_one({"title": title})
    return True