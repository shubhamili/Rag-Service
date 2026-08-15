from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"hello we are creatign rag seercive here"}