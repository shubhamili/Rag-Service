from fastapi import FastAPI
from app.routes.document_routes import router as document_router
app = FastAPI()


app.include_router(document_router)


@app.get("/")
def home():
    return {"message":"hello we are creatign rag seercive here"}