from pydantic import BaseModel

class Phrase(BaseModel):
    title: str
    word: str