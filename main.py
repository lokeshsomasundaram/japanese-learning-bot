from fastapi import FastAPI
from quiz import get_random_question

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "🇯🇵 Japanese Learning Bot is running!"
    }


@app.get("/quiz")
def quiz():
    question = get_random_question()

    return {
        "question": question["question"],
        "options": question["options"]
    }
