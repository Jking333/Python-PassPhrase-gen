import pydantic
import passPhrase as pp
import time
from fastapi import FastAPI
global passphrase_object
passphrase_object = pp.main()


app = FastAPI()


@app.get("/")
def home():
    return {'passphrase_object':f'{passphrase_object.__dict__}'}


