"""Dont run this yet, if you finish setting up your mongodb project connect and get the atlas connection string, then you can put: conn_str = 'your_atlas_string' """
import asyncio
import motor
async def get_server_info():
    """conn_str still needs to be setup. Mongodb is already created. Just need to finish connection setup."""
    conn_str = "myfirstcluster-shard-00-02.py8c0.mongodb.net:27017"

    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)

    try:
    
        print(await client.server_info())
    except Exception:
        print("Unable to connect to the server.")
loop = asyncio.get_event_loop()
loop.run_until_complete(get_server_info())