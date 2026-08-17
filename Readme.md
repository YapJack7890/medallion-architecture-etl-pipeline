# E-Commerce Analytics Platform
### End-to-End Data Engineering, Analytics & Machine Learning Pipeline

An enterprise-inspired data platform that transforms raw e-commerce data into analytics-ready datasets using a Medallion Architecture (Bronze, Silver, Gold). The platform supports business intelligence dashboards, dimensional modeling, and predictive machine learning for business decision-making.

---

## Project Overview

This project demonstrates the complete lifecycle of modern data engineering and analytics.

Starting from raw transactional data, the pipeline performs data ingestion, validation, cleaning, transformation, dimensional modeling, dashboard development, and machine learning.

The project is designed to mirror how data platforms are implemented in industry.

---

## Architecture

```
                    Data Source
              (Olist E-Commerce Dataset)
                           │
                           ▼
                 Python ETL Pipeline
                           │
                           ▼
               Bronze Layer (Raw Data)
                           │
                           ▼
            Silver Layer (Validated Data)
                           │
                           ▼
           Gold Layer (Business Models)
                           │
          ┌────────────────┴──────────────┐
          ▼                               ▼
   Power BI Dashboard             Machine Learning
```

---

# Features

### Data Engineering

- Python ETL Pipeline
- Medallion Architecture
- BigQuery Data Warehouse
- Data Validation
- Data Cleaning
- Incremental-ready Pipeline
- Modular Project Structure

### Data Warehouse

- Bronze Layer
- Silver Layer
- Gold Layer
- Star Schema
- Fact & Dimension Tables
- Data Dictionary

### Analytics

- Revenue Analysis
- Customer Analytics
- Product Performance
- Seller Performance
- Executive KPI Dashboard

### Machine Learning

- Customer Churn Prediction
- Customer Lifetime Value
- Sales Forecasting
- Delivery Delay Prediction
- Feature Engineering
- Model Evaluation

---

# Technology Stack

| Category | Technology |
|------------|------------|
| Language | Python |
| Data Warehouse | Google BigQuery |
| ETL | Pandas |
| SQL | BigQuery SQL |
| Dashboard | Power BI |
| Machine Learning | Scikit-learn, XGBoost |
| Version Control | Git |
| Documentation | Markdown |

---

# Project Structure

```
ecommerce-analytics-platform/

│

├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── notebooks/
│
├── pipelines/
│
├── sql/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── models/
│
├── dashboards/
│
├── docs/
│   ├── architecture.md
│   ├── medallion.md
│   ├── star_schema.md
│   ├── data_dictionary.md
│   ├── pipeline.md
│   └── dashboard.md
│
└── README.md
```

---

# Data Pipeline

The pipeline follows the Medallion Architecture.

```
CSV Files

↓

Bronze

↓

Validation

↓

Cleaning

↓

Silver

↓

Business Modeling

↓

Gold

↓

Power BI / Machine Learning
```

## Bronze

- Raw source data
- Immutable records
- Metadata tracking
- Audit trail

## Silver

- Data cleansing
- Standardization
- Validation
- Business rules

## Gold

- Fact tables
- Dimension tables
- KPI tables
- Aggregated datasets
- Analytics-ready models

---

# Data Warehouse Design

## Fact Tables

- fact_sales

## Dimension Tables

- dim_customer
- dim_product
- dim_seller
- dim_date

The warehouse is modeled using a Star Schema to improve analytical query performance and simplify business reporting.

---

# Dashboards

The project includes multiple Power BI dashboards.

### Executive Dashboard

- Revenue
- Orders
- Profit
- Average Order Value
- Monthly Growth

### Customer Dashboard

- Customer Lifetime Value
- Repeat Purchase Rate
- Geographic Distribution
- Customer Segmentation

### Product Dashboard

- Best Selling Products
- Category Performance
- Seller Performance
- Product Ratings

---

# Machine Learning

The Gold Layer provides clean feature tables for predictive analytics.

Current models include:

- Customer Churn Prediction
- Sales Forecasting
- Customer Lifetime Value Prediction
- Delivery Delay Prediction

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- RMSE
- MAE

---

# Documentation

Additional documentation is available in the `/docs` directory.

| Document | Description |
|-----------|-------------|
| architecture.md | Overall solution architecture |
| medallion.md | Bronze, Silver, Gold implementation |
| pipeline.md | ETL workflow |
| star_schema.md | Warehouse design |
| data_dictionary.md | Table & column definitions |
| dashboard.md | KPI definitions |

---

# Future Improvements

- Apache Airflow orchestration
- Incremental ETL
- Data Quality Framework
- Great Expectations integration
- Feature Store
- MLflow
- CI/CD
- Docker Deployment
- Real-time Kafka ingestion

---

# Learning Outcomes

This project demonstrates practical experience in:

- Data Engineering
- Data Warehousing
- SQL
- ETL Development
- Data Modeling
- Business Intelligence
- Machine Learning
- Software Engineering Best Practices

---

# License

This project is intended for educational and portfolio purposes.