import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = "http://localhost:8000/"

API_ENDPOINTS = {
    "GENERATE": f"{API_BASE_URL}/generate",
}

API_KEY = os.getenv("API_KEY")

print(API_KEY)
