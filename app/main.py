from fastapi import FastAPI
import os
from dotenv import load_dotenv
from app.routes.document_routes import router as document_router
app = FastAPI()

load_dotenv()
app.include_router(document_router)

api_key = os.getenv("GEMINI_API_KEY")


@app.get("/")
def home():
    print("api_key =============> ",api_key)
    return {"message":"hello we are creatign rag seercive here"}