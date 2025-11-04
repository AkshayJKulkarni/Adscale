from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn
import hashlib
import json

# Load trained model
model_data = joblib.load('models/adscale_model.pkl')
model = model_data['model']
encoder = model_data['encoder']

# Cache and stats
cache = {}
stats = {"total_requests": 0, "total_ctr": 0.0}

app = FastAPI(title="AdScale - Ad Performance Optimizer", version="1.0.0")

class AdInput(BaseModel):
    impressions: int
    ad_position: int
    device_type: str
    budget: float

class CTRPrediction(BaseModel):
    predicted_ctr: float

@app.post("/predict_ctr", response_model=CTRPrediction)
async def predict_ctr(ad_data: AdInput):
    # Create cache key
    cache_key = hashlib.md5(json.dumps(ad_data.dict(), sort_keys=True).encode()).hexdigest()
    
    # Check cache
    if cache_key in cache:
        prediction = cache[cache_key]
    else:
        device_encoded = encoder.transform([ad_data.device_type])[0]
        estimated_clicks = int(ad_data.impressions * 0.1085)
        
        features = np.array([[
            ad_data.impressions,
            estimated_clicks,
            ad_data.ad_position,
            device_encoded,
            ad_data.budget
        ]])
        
        prediction = round(model.predict(features)[0], 4)
        cache[cache_key] = prediction
    
    # Update stats
    stats["total_requests"] += 1
    stats["total_ctr"] += prediction
    
    return CTRPrediction(predicted_ctr=prediction)

class StatsResponse(BaseModel):
    total_requests: int
    average_predicted_ctr: float
    unique_cached_requests: int

@app.get("/stats", response_model=StatsResponse)
async def get_stats():
    avg_ctr = stats["total_ctr"] / stats["total_requests"] if stats["total_requests"] > 0 else 0.0
    return StatsResponse(
        total_requests=stats["total_requests"],
        average_predicted_ctr=round(avg_ctr, 4),
        unique_cached_requests=len(cache)
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)