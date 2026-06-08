# Automated E-Commerce Data Pipeline: Sales & Marketing Integration

## 📌 The Business Problem

A boutique e-commerce brand struggled to calculate their true daily profitability. Sales data was locked in a REST API, while marketing ad spend was scattered across flat CSV files, making daily reporting a slow, manual process prone to human error.

## 💡 The Solution

I engineered an automated Python ETL pipeline that extracts, cleans, and integrates daily sales and ad spend data into a centralized PostgreSQL database. This created a single source of truth, enabling automated, real-time reporting on key business metrics like Return on Ad Spend (ROAS) and Net Profit.

## 🛠️ Tech Stack

* **Language:** Python (Pandas)
* **Database:** PostgreSQL, SQLAlchemy
* **Architecture:** Modular ETL (Extract, Transform, Load)
* **Concepts:** Data aggregation, API simulation, Relational database design

## 📊 Business Outcomes

* **Eliminated Manual Reporting:** Replaced hours of manual spreadsheet merging with a single automated script.
* **Unified Data:** Merged disconnected marketing and sales data streams.
* **Actionable Insights:** Delivered clean, structured tables ready for visualization tools like Power BI or Tableau to track daily ROAS.

## 🚀 How to Run Locally

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Generate mock client data: `python src/generate_mock_data.py`
4. Update PostgreSQL credentials in `src/load.py`.
5. Execute the pipeline: `python main.py`

## Project Structure

```
ecommerce_etl_project/
│
├── data/                  
│   ├── raw/                 # Where our business CSVs and JSONs files will live
│
├── src/                   
│   ├── __init__.py          # Makes 'src' a Python module
│   ├── generate_mock_data.py # Script to create our fake client data
│   ├── extract.py           # Code to pull data from sources
│   ├── transform.py         # Pandas logic to clean and merge
│   └── load.py              # Database connection and insertion logic
│
├── main.py                  # The master script to run the whole pipeline
├── requirements.txt         # List of Python libraries needed (pandas, etc.)
├── .gitignore               # For skipping secrets
└── README.md                # The business case study
```
