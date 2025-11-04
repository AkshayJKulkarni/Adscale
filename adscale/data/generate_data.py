import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 5000

data = {
    'impressions': np.random.randint(100, 20000, n_samples),
    'clicks': np.random.randint(1, 1000, n_samples),
    'ad_position': np.random.randint(1, 11, n_samples),
    'device_type': np.random.choice(['mobile', 'desktop', 'tablet'], n_samples, p=[0.6, 0.3, 0.1]),
    'budget': np.random.uniform(50, 10000, n_samples).round(2)
}

df = pd.DataFrame(data)

# Ensure clicks don't exceed impressions
df['clicks'] = np.minimum(df['clicks'], df['impressions'])

# Calculate CTR
df['ctr'] = df['clicks'] / df['impressions']

# Save to CSV
df.to_csv('ad_data.csv', index=False)

# Print summary
print(f"Dataset generated with {len(df)} records")
print(f"CTR range: {df['ctr'].min():.4f} - {df['ctr'].max():.4f}")
print(f"Average CTR: {df['ctr'].mean():.4f}")
print(f"Device distribution:\n{df['device_type'].value_counts()}")