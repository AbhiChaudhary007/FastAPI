import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return 'Hey!!! First FastAPI'
