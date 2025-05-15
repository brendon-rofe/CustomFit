from pydantic import BaseModel

class PromptRequest(BaseModel):
  prompt: str

class CalorieCalculationRequest(BaseModel):
	gender: str
	age: int
	height: float
	weight: float
