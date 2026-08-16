from fastapi import UploadFile,File


async def upload_doc(file:UploadFile = File(...)):
    return{
        "filename":file.filename
    }