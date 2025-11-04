import aiohttp
import asyncio
import random
import json

async def send_request(session, request_id):
    data = {
        "impressions": random.randint(100, 20000),
        "ad_position": random.randint(1, 10),
        "device_type": random.choice(["mobile", "desktop", "tablet"]),
        "budget": round(random.uniform(50, 10000), 2)
    }
    
    async with session.post("http://localhost:8000/predict_ctr", json=data) as response:
        result = await response.json()
        print(f"Request {request_id}: CTR = {result['predicted_ctr']:.4f}")
        return result

async def simulate_concurrent_requests():
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, i+1) for i in range(50)]
        results = await asyncio.gather(*tasks)
        
        ctrs = [r['predicted_ctr'] for r in results]
        print(f"\nSummary: {len(results)} requests completed")
        print(f"CTR range: {min(ctrs):.4f} - {max(ctrs):.4f}")
        print(f"Average CTR: {sum(ctrs)/len(ctrs):.4f}")

if __name__ == "__main__":
    asyncio.run(simulate_concurrent_requests())