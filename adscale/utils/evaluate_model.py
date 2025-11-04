import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

# Load data and model
df = pd.read_csv('../data/ad_data.csv')
model_data = joblib.load('../models/adscale_model.pkl')
model = model_data['model']
encoder = model_data['encoder']

# Prepare features
df['device_encoded'] = encoder.transform(df['device_type'])
X = df[['impressions', 'clicks', 'ad_position', 'device_encoded', 'budget']]
y = df['ctr']

# Split data (same split as training)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Predict on test set
y_pred = model.predict(X_test)

# Calculate metrics
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Model Evaluation Metrics:")
print(f"R² Score: {r2:.4f}")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")