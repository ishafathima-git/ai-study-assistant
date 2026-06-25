from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

class PromptRequest(BaseModel):
    prompt: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/generate")
async def generate(data: PromptRequest):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
    {
        "role":"system",
        "content":"You are a helpful academic study assistant. Give clear and concise educational answers."
    },
    {
        "role":"user",
        "content":data.prompt
    }
]
    )

    return {
        "response":
        response.choices[0].message.content
    }