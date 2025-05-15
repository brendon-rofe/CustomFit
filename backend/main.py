from fastapi import FastAPI
import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompt import *
import json
import re

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
  data.prompt += " If what I have just said is not health and fitness related, please respond by saing 'I am sorry, but can you please stick to health and fitness questions.'"
  response = model.generate_content(data.prompt)
  return {"response": response.text}

@app.post("/calorie-calculator")
def calculate_calories(data: CalorieCalculationRequest):
  prompt = (
    f"Please calculate and return to me the daily calorie needs for someone with the following criteria: "
    f"{data.gender}, {data.age} years old, {data.height}cm tall, {data.weight}kg. "
    f"Return the answer in raw JSON using this structure: "
    f'{{"calories": number, "protein_g": number, "carbs_g": number, "fat_g": number}}.'
  )
  response = model.generate_content(prompt)
  raw_text = response.text

  cleaned = re.sub(r"^```json\n|\n```$", "", raw_text.strip())
  parsed = json.loads(cleaned)

  return parsed
