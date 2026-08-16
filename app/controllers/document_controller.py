from fastapi import UploadFile,File
from app.services.chunk_service import chunk_Text
import pymupdf

async def upload_doc(file:UploadFile = File(...)):

    doc = pymupdf.open(stream = file.file.read(),filetype=file.content_type)

    extractedText = ""

    for page in doc:
        extractedText += page.get_text()

    chuks =  chunk_Text(extractedText,500,100)
    print(chuks)
    return{
        "filename":file.filename,
        # "extractedText":extractedText,
        "chuks":chuks,
        "chuks length":len(chuks)
    }