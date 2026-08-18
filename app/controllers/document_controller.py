from fastapi import UploadFile,File
from app.services.chunk_service import chunk_Text
from app.services.embedding_service import generateEmbedding
import pymupdf

async def upload_doc(file:UploadFile = File(...)):

    doc = pymupdf.open(stream = file.file.read(),filetype=file.content_type)

    extractedText = ""

    for page in doc:
        extractedText += page.get_text()

    chuks =  chunk_Text(extractedText,500,100)


    embedData =   generateEmbedding(chuks)

    print("len(embedData.embeddings) =>",len(embedData.embeddings))
    print("len(embedData.embeddings[0].values) =>",len(embedData.embeddings[0].values))



    # print(chuks)
    return{
        "filename":file.filename,
        # "extractedText":extractedText,
        "chuks":chuks,
        "chuks length":len(chuks),
        "embedData":embedData
    }