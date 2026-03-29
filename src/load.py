import pandas as pd
from sqlalchemy import create_engine, text

def create_db_if_not_exists(username, password, db_name):
    """Connects to the default database to create the target database if it is missing."""
    # Connect to the default 'postgres' database with AUTOCOMMIT
    default_engine = create_engine(
        f'postgresql://{username}:{password}@localhost:5432/postgres', 
        isolation_level='AUTOCOMMIT'
    )
    
    with default_engine.connect() as conn:
        # Check if our target database already exists
        result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'"))
        if not result.fetchone():
            print(f"Database '{db_name}' not found. Creating it automatically...")
            conn.execute(text(f"CREATE DATABASE {db_name}"))
        else:
            print(f"Database '{db_name}' already exists.")

def load_data(df, table_name):
    """Loads transformed data into the PostgreSQL database."""
    username = 'postgres'      
    password = 'postgres' # REPLACE with your actual local password
    db_name = 'ecommerce_db'   
    
    # 1. Ensure the database exists
    create_db_if_not_exists(username, password, db_name)
    
    # 2. Connect to the target database and load the data
    print(f"Loading {len(df)} records into '{table_name}'...")
    engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/{db_name}')
    
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Successfully loaded data into the '{table_name}' table!")

if __name__ == "__main__":
    print("This module is meant to be run from main.py")