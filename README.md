# AdScale - Ad Performance Optimizer

A FastAPI-based ML service that predicts ad click-through rates (CTR) using Random Forest regression with in-memory caching.

## Local Setup

```bash
cd adscale
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
```

## Docker Setup

```bash
docker build -t adscale .
docker run -p 8000:8000 adscale
```

## API Usage

**Predict CTR:**
```bash
POST /predict_ctr
{
  "impressions": 5000,
  "ad_position": 1,
  "device_type": "mobile",
  "budget": 2500.0
}
```

**Response:**
```json
{"predicted_ctr": 0.0847}
```

**Get Stats:**
```bash
GET /stats
```

API docs: `http://localhost:8000/docs`