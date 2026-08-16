from fastapi import UploadFile,File
import pymupdf

async def upload_doc(file:UploadFile = File(...)):

    doc = pymupdf.open(stream = file.file.read(),filetype=file.content_type)

    extractedText = ""

    for page in doc:
        extractedText += page.get_text()

    docExtracted = extractedText

    print("____________docExtracted =================>",docExtracted)

    return{
        "filename":file.filename,
        "docExtracted":docExtracted
    }