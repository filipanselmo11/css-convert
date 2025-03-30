from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods
        allow_headers=["*"],  # Allows all headers
    )