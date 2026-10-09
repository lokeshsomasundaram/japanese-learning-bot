from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from quiz import get_random_question

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/quiz")
def quiz():
    question = get_random_question()
    return {
        "question": question["question"],
        "options": question["options"],
        "answer": question["answer"]
    }
