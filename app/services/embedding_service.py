from google import genai
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("client =>",client)


def generateEmbedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text
    )
    print("result =>",result)
    print("result.embeddings",result.embeddings)
    return result