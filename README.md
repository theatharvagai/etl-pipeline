<div align="center">

# 📈 Automated Financial Data ETL Pipeline

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&pause=1000&color=00F72D&center=true&vCenter=true&width=650&lines=Production+Grade+ETL+Pipeline;Stock+Market+Data+Automation;Python+%7C+PostgreSQL+%7C+Pandas+%7C+SQLAlchemy" />

<br>

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.2-orange.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-green.svg)
![Docker](https://img.shields.io/badge/docker-supported-blue)

</div>

---

# 📊 Repository Stats

<div align="center">

### 👀 Visitors

![Visitors](https://api.visitorbadge.io/api/visitors?path=theatharvagai/etl-pipeline&countColor=%23263759)

<br>

### 📈 GitHub Stats

![GitHub stats](https://github-readme-stats.vercel.app/api?username=theatharvagai&show_icons=true&theme=tokyonight)

<br>

### 🔥 Most Used Languages

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=theatharvagai&layout=compact&theme=tokyonight)

</div>

---

# 📊 Project Overview

This project implements a **production-style Financial Data ETL Pipeline** that automatically:

✔ Extracts historical stock market data  
✔ Performs financial transformations  
✔ Loads processed datasets into PostgreSQL  

The system enables **analytics, financial insights, and automated data pipelines**.

---

# ⚙️ ETL Pipeline Architecture

```
        +-------------+
        | yFinance API|
        +------|------+
               |
               v
        +-------------+
        |   Extract   |
        | Fetch OHLCV |
        +------|------+
               |
               v
        +-------------+
        | Transform   |
        | Pandas Data |
        | Indicators  |
        +------|------+
               |
               v
        +-------------+
        | Load        |
        | PostgreSQL  |
        +-------------+
```

---

# ✨ Features

## 📥 Extraction
- Pulls **historical OHLCV stock data**
- Supports configurable tickers
- Uses **yfinance API**

## 🔄 Transformation
Financial indicators computed:

- 7-Day Moving Average
- 30-Day Moving Average
- Daily Returns
- Rolling Volatility

## 📤 Loading
- PostgreSQL database
- Upsert logic
- SQLAlchemy ORM

---

# 🖼️ Screenshots

## Pipeline Execution

<p align="center">
<img src="./Screenshot 2026-03-16 001839.png" width="850">
</p>

---

## Database Output

<p align="center">
<img src="./Screenshot 2026-03-16 001927.png" width="850">
</p>

---

# 📁 Project Structure

```
etl-pipeline/

├── analytics/
│   └── sample_queries.sql
│
├── config/
│   └── config.yaml
│
├── data/
│
├── db/
│   ├── db_connection.py
│   └── schema.sql
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── tests/
│   └── test_pipeline.py
│
├── .env
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/theatharvagai/etl-pipeline.git
cd etl-pipeline
```

---

# 🔐 Configure Environment Variables

Create `.env`

```
DB_PASSWORD=your_secure_password
```

---

# 📦 Install Dependencies

```bash
python -m venv venv

source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

---

# 🗄️ Database Setup

Ensure **PostgreSQL** is running.

Update configuration in:

```
config/config.yaml
```

The pipeline automatically creates the table:

```
stock_prices
```

---

# ▶️ Running the Pipeline

```bash
python main.py
```

---

# 🧪 Run Tests

```bash
pytest tests/
```

---

# ⏱️ Scheduling with Cron

Run pipeline daily at **6 AM**

```bash
crontab -e
```

Add:

```
0 6 * * * /path/to/venv/bin/python /path/to/project/main.py >> pipeline.log 2>&1
```

---

# 🐳 Docker Support

Build container

```bash
docker build -t etl-pipeline .
```

Run container

```bash
docker run --env-file .env etl-pipeline
```

---

# 📊 Example Analytics Queries

### Average Daily Return

```sql
SELECT ticker, AVG(daily_return)
FROM stock_prices
GROUP BY ticker;
```

### Volatility Ranking

```sql
SELECT ticker, AVG(volatility)
FROM stock_prices
GROUP BY ticker
ORDER BY 2 DESC;
```

---

# 🚀 Future Improvements

- Apache Airflow orchestration  
- Kafka streaming pipeline  
- Streamlit dashboard  
- Grafana monitoring  
- Additional indicators (RSI, MACD)

---

<div align="center">

### ⭐ If you like this project, give it a star!

</div>
