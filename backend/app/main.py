from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.fetch_stats import load_merged_stats

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load the merged data once
merged_data = load_merged_stats()

@app.get("/test-merge")
def test_merge():
    # Return basic metadata to confirm successful merge
    return {
        "num_teams": len(merged_data),
        "num_columns": len(merged_data.columns),
        "columns": list(merged_data.columns)[:10],  # Preview first 10 columns
    }