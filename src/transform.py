import pandas as pd
from src.extract import extract_sales_data, extract_ad_spend

def transform_data(sales_df, ad_df):
    """Cleans, merges, and transforms the raw data into business metrics."""
    print("Starting data transformation...")
    
    # 1. Clean Sales Data: Keep only 'completed' orders
    completed_sales = sales_df[sales_df['status'] == 'completed']
    
    # 2. Aggregate Sales: Get total daily revenue
    daily_revenue = completed_sales.groupby('date')['revenue'].sum().reset_index()
    daily_revenue.rename(columns={'revenue': 'total_revenue'}, inplace=True)
    
    # 3. Aggregate Ad Spend: Get total daily spend across all campaigns
    daily_spend = ad_df.groupby('date')['spend'].sum().reset_index()
    daily_spend.rename(columns={'spend': 'total_ad_spend'}, inplace=True)
    
    # 4. Merge Data: Join revenue and spend on the 'date' column
    merged_df = pd.merge(daily_revenue, daily_spend, on='date', how='inner')
    
    # 5. Business Logic: Calculate Return on Ad Spend (ROAS)
    # ROAS = Revenue / Ad Spend
    merged_df['roas'] = (merged_df['total_revenue'] / merged_df['total_ad_spend']).round(2)
    
    # 6. Calculate Net Profit (Revenue - Spend)
    merged_df['net_profit'] = (merged_df['total_revenue'] - merged_df['total_ad_spend']).round(2)
    
    print(f"Transformation complete. Final dataset has {len(merged_df)} daily records.")
    return merged_df

if __name__ == "__main__":
    # Load raw data using your extract module
    sales_file = '../data/raw/sales_api_response.json'
    ad_file = '../data/raw/ad_spend.csv'
    
    raw_sales = extract_sales_data(sales_file)
    raw_ads = extract_ad_spend(ad_file)
    
    # Run the transformation
    final_dataset = transform_data(raw_sales, raw_ads)
    
    # Preview the clean, business-ready data
    print("\n--- Final Transformed Data (Business Metrics) ---")
    print(final_dataset.head())