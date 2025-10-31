from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Allow frontend (Streamlit) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "✅ FastAPI backend deployed successfully on Render!"}

@app.get("/analyze")
def analyze(city: str):
    # Dummy example data (replace later with your real logic)
    data = {
        "avg_temp": 34.7,
        "uhi_index": 2.5,
        "temperature_series": [
            {"date": "2025-10-25", "temperature": 33.2},
            {"date": "2025-10-26", "temperature": 34.5},
            {"date": "2025-10-27", "temperature": 35.1},
            {"date": "2025-10-28", "temperature": 34.9},
            {"date": "2025-10-29", "temperature": 36.2},
            {"date": "2025-10-30", "temperature": 35.4},
            {"date": "2025-10-31", "temperature": 34.8},
        ],
    }
    return JSONResponse(content=data)
