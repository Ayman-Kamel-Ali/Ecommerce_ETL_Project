import pandas as pd
import json

def extract_sales_data(file_path):
    """Extracts sales data from a JSON file (simulating an API response)."""
    print(f"Extracting sales data from {file_path}...")
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    print(f"Successfully extracted {len(df)} sales records.")
    return df

def extract_ad_spend(file_path):
    """Extracts ad spend data from a CSV file."""
    print(f"Extracting ad spend data from {file_path}...")
    df = pd.read_csv(file_path)
    print(f"Successfully extracted {len(df)} ad spend records.")
    return df

if __name__ == "__main__":
    # Test the extraction process
    sales_file = '../data/raw/sales_api_response.json'
    ad_file = '../data/raw/ad_spend.csv'
    
    sales_df = extract_sales_data(sales_file)
    ad_df = extract_ad_spend(ad_file)
    
    # Preview the data to ensure it loaded correctly
    print("\n--- Sales Data Preview ---")
    print(sales_df.head(3))
    
    print("\n--- Ad Spend Data Preview ---")
    print(ad_df.head(3))