# Automated Financial Data ETL Pipeline for Stock Market Analytics

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.2.0-orange.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.25-green.svg)

## Project Overview

This project is a complete, production-grade **Financial Data ETL Pipeline** designed to automate the extraction of historical stock market data, perform advanced financial transformations, and load the processed datasets into a PostgreSQL database for downstream analytics.

## Architecture

1.  **Extraction**: Historical OHLCV (Open, High, Low, Close, Volume) data is fetched for a configurable list of tickers (e.g., AAPL, MSFT, GOOGL) using the `yfinance` API.
2.  **Transformation**: Data is cleaned using `pandas`, handling missing values and duplicates. Financial indicators such as 7-day/30-day Moving Averages, Daily Returns, and Rolling Volatility are calculated.
3.  **Loading**: The transformed data is loaded into a PostgreSQL database using an "upsert" mechanism (using `SQLAlchemy` and `psycopg2`) to ensure no duplicate records exist for any given ticker and date.

## Project Structure

```text
financial-etl-pipeline/
│
├── analytics/           # Example SQL queries for data analysis
│   └── sample_queries.sql
├── config/              # YAML configuration files
│   └── config.yaml
├── data/                # Directory for local data exports (if any)
├── db/                  # Database schema and connection logic
│   ├── db_connection.py
│   └── schema.sql
├── etl/                 # Core ETL logic (Extract, Transform, Load)
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
├── tests/               # Automated unit tests
│   └── test_pipeline.py
├── .env                 # Environment variables (DB credentials)
├── Dockerfile           # Containerization configuration
├── main.py              # Main entry point for the pipeline
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/financial-etl-pipeline.git
cd financial-etl-pipeline
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory (or update the provided one):
```text
DB_PASSWORD=your_secure_password
```

### 3. Install Dependencies
It's recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Database Setup
Ensure you have a PostgreSQL instance running. You can update the database settings in `config/config.yaml`. The pipeline will automatically create the `stock_prices` table if it doesn't exist.

## Running the Pipeline

To execute the full ETL process:
```bash
python main.py
```

To run unit tests:
```bash
pytest tests/
```

## Scheduling with Cron

To run the pipeline every day at 6 AM:
1. Open your crontab:
   ```bash
   crontab -e
   ```
2. Add the following line (update paths as needed):
   ```text
   0 6 * * * /path/to/venv/bin/python /path/to/project/main.py >> /path/to/project/pipeline.log 2>&1
   ```

## Docker Support

Build and run the pipeline inside a container:
```bash
docker build -t financial-etl-pipeline .
docker run --env-file .env financial-etl-pipeline
```

## Example Analytics Queries

After running the pipeline, you can run these queries in your PostgreSQL terminal:

*   **Average Daily Return per Stock**
    ```sql
    SELECT ticker, AVG(daily_return) FROM stock_prices GROUP BY ticker;
    ```
*   **Volatility Ranking**
    ```sql
    SELECT ticker, AVG(volatility) FROM stock_prices GROUP BY ticker ORDER BY 2 DESC;
    ```

## Future Improvements

*   Integrate with Apache Airflow for advanced orchestration.
*   Add more technical indicators (RSI, Bollinger Bands, MACD).
*   Implement real-time data streaming using Kafka.
*   Build a dashboard using Streamlit or Grafana.
