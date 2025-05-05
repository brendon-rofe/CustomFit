from fastapi import FastAPI
import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompt import PromptRequest

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to CustomFit API!"}

@app.post("/ask")
def ask_ai(data: PromptRequest):
  response = model.generate_content(data.prompt)
  return {"response": response.text}
