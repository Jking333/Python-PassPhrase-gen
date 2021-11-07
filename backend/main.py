import pydantic
import passPhrase as pp
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
global passphrase_object
passphrase_object = pp.main()

# App object
app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True, 
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def read_root():
    return{'passphrase_object':f'{passphrase_object.__dict__}'}

@app.get("api/phrase")
async def get_phrase(id):
    return 1

@app.post("api/phrase")
async def post_phrase(phrase):
    return 1

@app.put("api/phrase{id}")
async def put_phrase(id, data):
    return 1

@app.delete("api/phrase")
async def delete_phrase(id, data):
    return 1
