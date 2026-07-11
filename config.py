import os
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
model_name = os.getenv("MODEL_NAME")
debug = os.getenv("DEBUG")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is missing.")

if not model_name:
    raise ValueError("MODEL_NAME is missing.")

if debug is None:
    raise ValueError("DEBUG is missing.")

debug = debug.lower() == "true"

class Config:
    GOOGLE_API_KEY = google_api_key
    MODEL_NAME = model_name
    DEBUG = debug
