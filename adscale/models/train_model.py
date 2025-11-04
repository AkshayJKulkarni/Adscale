import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

# Load data
df = pd.read_csv('../data/ad_data.csv')

# Encode categorical fields
le = LabelEncoder()
df['device_encoded'] = le.fit_transform(df['device_type'])

# Features and target
X = df[['impressions', 'clicks', 'ad_position', 'device_encoded', 'budget']]
y = df['ctr']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"Model R² score: {r2:.4f}")

# Save model and encoder
joblib.dump({'model': model, 'encoder': le}, 'adscale_model.pkl')
print("Model saved as adscale_model.pkl")