#!/bin/bash
export MODEL_PATH="models/your-llama-model.gguf"
uvicorn app:app --host 0.0.0.0 --port 8000
