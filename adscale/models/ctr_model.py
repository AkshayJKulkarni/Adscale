import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import os

class CTRPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.device_encoder = LabelEncoder()
        self.is_trained = False
        self._train_model()
    
    def _train_model(self):
        # Generate synthetic training data
        np.random.seed(42)
        n_samples = 1000
        
        data = {
            'impressions': np.random.randint(100, 10000, n_samples),
            'clicks': np.random.randint(1, 500, n_samples),
            'ad_position': np.random.randint(1, 11, n_samples),
            'device_type': np.random.choice(['mobile', 'desktop', 'tablet'], n_samples),
            'budget': np.random.uniform(100, 5000, n_samples)
        }
        
        df = pd.DataFrame(data)
        df['ctr'] = df['clicks'] / df['impressions']
        
        # Encode device type
        df['device_encoded'] = self.device_encoder.fit_transform(df['device_type'])
        
        # Features
        X = df[['impressions', 'clicks', 'ad_position', 'device_encoded', 'budget']]
        y = df['ctr']
        
        self.model.fit(X, y)
        self.is_trained = True
    
    def predict(self, ad_data):
        if not self.is_trained:
            raise ValueError("Model not trained")
        
        # Encode device type
        device_encoded = self.device_encoder.transform([ad_data['device_type']])[0]
        
        features = np.array([[
            ad_data['impressions'],
            ad_data['clicks'],
            ad_data['ad_position'],
            device_encoded,
            ad_data['budget']
        ]])
        
        prediction = self.model.predict(features)[0]
        return max(0, min(1, prediction))  # Clamp between 0 and 1