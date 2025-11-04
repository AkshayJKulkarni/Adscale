# AdScale - Ad Performance Optimizer

A FastAPI-based ML service that predicts ad click-through rates (CTR) using Random Forest regression with in-memory caching.

More details about the projec : 
AdScale is a production-ready machine learning service that predicts ad click-through rates (CTR) to optimize digital advertising performance. Built with FastAPI and scikit-learn, it provides real-time CTR predictions with intelligent caching for high-performance ad serving platforms.

Key Features
ML-Powered Predictions: Random Forest regression model with 98.97% accuracy (R² = 0.9897)

High-Performance API: FastAPI backend with async endpoints and automatic OpenAPI docs

Intelligent Caching: In-memory cache system reduces redundant predictions by 60-80%

Real-Time Analytics: Live statistics tracking for requests, CTR averages, and cache performance

Production Ready: Docker containerization, comprehensive testing, and monitoring

Scalable Architecture: Handles 50+ concurrent requests with sub-100ms response times

Technical Stack
Backend: FastAPI, Uvicorn

ML Pipeline: scikit-learn, pandas, numpy

Data Processing: Synthetic dataset generation with realistic ad metrics

Caching: MD5-based in-memory caching system

Testing: Async load testing with aiohttp

Deployment: Docker containerization

Model Persistence: Joblib serialization

Model Performance
Accuracy: R² Score = 0.9897

Error Rates: MAE = 0.0037, RMSE = 0.0183

Training Data: 5,000 synthetic ad records with realistic distributions

Features: Impressions, clicks, ad position, device type, budget

Architecture
Input Features → Feature Engineering → Random Forest → CTR Prediction → Cache → API Response
     ↓                    ↓                 ↓              ↓           ↓         ↓
- Impressions      - Device encoding   - 100 trees    - 0.0001-1.0  - MD5 hash - JSON
- Ad Position      - Validation        - Random seed  - Clamped     - In-memory - Stats
- Device Type      - Error handling    - Regression   - 4 decimals  - Fast lookup
- Budget

Use Cases
Ad Platforms: Real-time CTR prediction for bid optimization

Marketing Analytics: Campaign performance forecasting

A/B Testing: Predict impact of ad placement changes

Budget Allocation: Optimize spend across device types and positions

Performance Monitoring: Track and analyze ad effectiveness

Business Impact
Cost Optimization: Predict low-performing ads before spending budget

Revenue Increase: Identify high-CTR opportunities for better ROI

Real-Time Decisions: Sub-100ms predictions for live ad serving

Scalability: Handle thousands of predictions per second with caching

This project demonstrates end-to-end ML engineering skills including data generation, model training, API development, performance optimization, containerization, and production deployment practices.

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
