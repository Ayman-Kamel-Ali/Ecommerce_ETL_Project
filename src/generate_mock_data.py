import json
import csv
import random
from datetime import datetime, timedelta
import os

# Ensure the raw data directory exists
os.makedirs('../data/raw', exist_ok=True)

# Generate Dates for the last 30 days
base_date = datetime.today()
dates = [(base_date - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(30)]

# 1. Generate Mock Sales Data (JSON - Simulating an API response)
sales_data = []
for i in range(200):
    sales_data.append({
        "order_id": f"ORD{1000+i}",
        "date": random.choice(dates),
        "revenue": round(random.uniform(20.0, 500.0), 2),
        "status": random.choices(["completed", "refunded"], weights=[0.9, 0.1])[0]
    })

with open('../data/raw/sales_api_response.json', 'w') as f:
    json.dump(sales_data, f, indent=4)

# 2. Generate Mock Marketing Spend (CSV - Simulating a flat file export)
with open('../data/raw/ad_spend.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['date', 'campaign', 'spend'])
    for date in dates:
        writer.writerow([date, 'Google Ads', round(random.uniform(50.0, 150.0), 2)])
        writer.writerow([date, 'Facebook Ads', round(random.uniform(40.0, 120.0), 2)])

print("Mock data generated successfully in data/raw/")