import pandas as pd
import numpy as np

def validate_ad_data(data):
    """Validate input ad data"""
    required_fields = ['impressions', 'clicks', 'ad_position', 'device_type', 'budget']
    
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    
    if data['clicks'] > data['impressions']:
        raise ValueError("Clicks cannot exceed impressions")
    
    if data['ad_position'] < 1 or data['ad_position'] > 10:
        raise ValueError("Ad position must be between 1 and 10")
    
    if data['device_type'] not in ['mobile', 'desktop', 'tablet']:
        raise ValueError("Device type must be mobile, desktop, or tablet")
    
    return True

def calculate_ctr(impressions, clicks):
    """Calculate click-through rate"""
    return clicks / impressions if impressions > 0 else 0