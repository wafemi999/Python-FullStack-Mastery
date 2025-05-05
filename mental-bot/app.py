from fastapi import FastAPI
from pydantic import BaseModel
from model.chat_with_bot import classifier
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

# cors middleware setting
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class Message(BaseModel):
    text: str

@app.post("/predict")
def predict_emotion(msg: Message):
    prediction, recommendation = classifier(msg.text)
    return {
        "prediction": prediction,
        "recommendation": recommendation
    }
