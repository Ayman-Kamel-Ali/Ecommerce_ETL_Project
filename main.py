from src.extract import extract_sales_data, extract_ad_spend
from src.transform import transform_data
from src.load import load_data

def run_pipeline():
    print("=== Starting E-Commerce ETL Pipeline ===")
    
    # 1. Extract
    sales_df = extract_sales_data('data/raw/sales_api_response.json')
    ad_df = extract_ad_spend('data/raw/ad_spend.csv')
    
    # 2. Transform
    business_metrics_df = transform_data(sales_df, ad_df)
    
    # 3. Load
    load_data(business_metrics_df, 'daily_marketing_metrics')
    
    print("=== Pipeline Execution Complete ===")

if __name__ == "__main__":
    run_pipeline()