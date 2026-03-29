import pandas as pd
import yaml
from sqlalchemy import create_engine, text

def create_db_if_not_exists(username, password, host, port, db_name):
    """Connects to the default database to create the target database if it is missing."""
    default_engine = create_engine(
        f'postgresql://{username}:{password}@{host}:{port}/postgres', 
        isolation_level='AUTOCOMMIT'
    )
    
    with default_engine.connect() as conn:
        result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'"))
        if not result.fetchone():
            print(f"Database '{db_name}' not found. Creating it automatically...")
            conn.execute(text(f"CREATE DATABASE {db_name}"))
        else:
            print(f"Database '{db_name}' already exists.")

def load_config(filename="config.yaml"):
    """Loads a YAML file into a Python dictionary."""
    with open(filename, 'r') as file:
        return yaml.safe_load(file) 

def load_data(df, table_name):
    """Loads transformed data into the PostgreSQL database."""
    # Config loaded only when the function is called, preventing import crashes
    config = load_config() 
    
    username = config['database']['user']      
    password = config['database']['password'] 
    db_name = config['database']['name']
    host = config['database']['host']
    port = config['database']['port']
    
    # Passing host and port dynamically
    create_db_if_not_exists(username, password, host, port, db_name)
    
    print(f"Loading {len(df)} records into '{table_name}'...")
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db_name}')
    
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Successfully loaded data into the '{table_name}' table!")

if __name__ == "__main__":
    print("This module is meant to be run from main.py")