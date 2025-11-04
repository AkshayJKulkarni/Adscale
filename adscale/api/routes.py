from fastapi import APIRouter
from pydantic import BaseModel
from models.ctr_model import CTRPredictor

router = APIRouter()
predictor = CTRPredictor()

class AdData(BaseModel):
    impressions: int
    clicks: int
    ad_position: int
    device_type: str
    budget: float

class CTRPrediction(BaseModel):
    predicted_ctr: float

@router.post("/predict", response_model=CTRPrediction)
async def predict_ctr(ad_data: AdData):
    ctr = predictor.predict(ad_data.dict())
    return CTRPrediction(predicted_ctr=ctr)

@router.get("/health")
async def health_check():
    return {"status": "healthy"}