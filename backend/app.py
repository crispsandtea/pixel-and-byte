from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.prompts import pixel_prompt, byte_prompt
from llama_cpp import Llama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = Llama(model_path="models/your-llama-model.gguf")

@app.get("/dialogue")
def get_dialogue():
    pixel_line = llm(pixel_prompt).strip()
    byte_line = llm(byte_prompt).strip()
    return {"pixel": pixel_line, "byte": byte_line}
