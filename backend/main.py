from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import openai
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

class URLCheckRequest(BaseModel):
    url: str

@app.get("/")
async def read_root():
    return {"message": "Phishing Detector API is online!"}

@app.post("/check_url")
async def check_url(request: URLCheckRequest):
    prompt = f"Check if the following URL is a phishing site: {request.url}. Answer in Yes or No."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a cybersecurity analyst whose expertise lies in analyzing websites URL and detect if that is a phishing site or not."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"result": response.choices[0].message['content']}

