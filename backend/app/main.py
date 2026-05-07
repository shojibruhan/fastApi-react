from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Fruit(BaseModel):
    name: str

class FruitResponse(BaseModel):
    fruits: List[Fruit]

origins= [
    "http://localhost:5173"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_methods= ['*'],
    allow_headers= ['*']
)

db= {
    "fruits": []
}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/fruits")
def create_fruit(fruit: Fruit):
    db["fruits"].append(fruit)
    return fruit

@app.get("/fruits", response_model= FruitResponse)
def get_fruits():
    return FruitResponse(fruits= db["fruits"])

