from fastapi import APIRouter
from app.controllers.document_controller import upload_doc

router = APIRouter(prefix="/doc", tags=["documents"]);


router.post('/upload')(upload_doc)