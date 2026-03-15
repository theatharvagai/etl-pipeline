import os
import yaml
import logging
import sys
import pandas as pd
from sqlalchemy import create_engine, text

# Add current directory to path so we can import from etl and db
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from etl.extract import extract_stock_data
from etl.transform import transform_stock_data

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("DemoRun")

def demo_run():
    logger.info("Starting Demo Run with SQLite...")
    
    # 1. Use a subset of tickers and shorter period for demo
    tickers = ["AAPL", "MSFT"]
    period = "1mo"
    interval = "1d"
    
    try:
        # 2. Extract
        logger.info(f"Extracting data for {tickers}...")
        df = extract_stock_data(tickers, period, interval)
        if df.empty:
            logger.error("No data extracted.")
            return

        # 3. Transform
        logger.info("Transforming data...")
        df_transformed = transform_stock_data(df)
        
        # 4. Load into SQLite (Demo)
        logger.info("Loading into SQLite (demo_financial.db)...")
        engine = create_engine("sqlite:///demo_financial.db")
        
        # Create table schema for SQLite
        with engine.connect() as conn:
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS stock_prices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticker TEXT,
                    date DATE,
                    open REAL,
                    high REAL,
                    low REAL,
                    close REAL,
                    adj_close REAL,
                    volume INTEGER,
                    daily_return REAL,
                    percentage_change REAL,
                    ma_7 REAL,
                    ma_30 REAL,
                    volatility REAL,
                    UNIQUE (ticker, date)
                )
            """))
            conn.commit()

        # Load data using pandas to_sql (simple for demo)
        df_transformed.to_sql("stock_prices", engine, if_exists="append", index=False)
        
        logger.info("Demo Run Completed Successfully!")
        
        # 5. Show sample from DB
        with engine.connect() as conn:
            result = conn.execute(text("SELECT ticker, date, close, daily_return FROM stock_prices LIMIT 5"))
            logger.info("Sample data from database:")
            for row in result:
                logger.info(row)
                
    except Exception as e:
        logger.error(f"Demo failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    demo_run()
