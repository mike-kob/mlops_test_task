import joblib
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
model = joblib.load('model.joblib')


class Query(BaseModel):
    text: str


@app.post("/")
async def root(query: Query):
    print(type(model.predict([query.text])[0]), "BLA")
    return {
        "target": model.predict([query.text])[0]
    }
