from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from csv_parser import parse_csv
from categorize import categorize_expenses
from roast import get_roast

app = FastAPI()

# Enable CORS for frontend later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    df = parse_csv(await file.read())
    categorized = categorize_expenses(df)
    roast = get_roast(categorized)
    return {
        "data": categorized.to_dict(orient="records"),
        "roast": roast
    }