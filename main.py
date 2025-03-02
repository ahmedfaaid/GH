import ollama
from fastapi import FastAPI

app = FastAPI()

@app.post("/chat")
def chat(query: str):
  response = ollama.chat(model='mistral', messages=[{"role": "user", "content": query}])
  return {"response": response["message"]["content"]}
