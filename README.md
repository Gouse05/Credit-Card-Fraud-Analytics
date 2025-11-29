# Credit Card Fraud Analytics – End-to-End ETL + Power BI Dashboard

This project identifies fraudulent transactions using data cleaning, feature engineering, ETL, and a fully interactive multi-page Power BI dashboard for audit analytics and merchant profiling.

## 🚀 Project Overview
This project focuses on analyzing transaction behaviors to detect anomalies and fraud patterns.  
It includes:
- Large-scale ETL & data cleaning (Python)
- Feature engineering (Risk Score, Anomaly detection, Month fields)
- Multi-page Power BI dashboard
- Merchant drill-through summary
- Fraud pattern analysis & risk segmentation

## 🛠️ Tech Stack
- Python (Pandas, NumPy)
- Power BI (Visualization)
- Git & GitHub (Version control)

## 📂 Repository Structure
Credit-Card-Fraud-Analytics/
│── etl_cleaning.py  
│── README.md  
│── fraudTrain.csv (excluded due to size)  
│── transactions_cleaned.csv (excluded due to size)  
│── images/  
│     ├── Screenshot 2025-11-29 013437.png  
│     ├── Screenshot 2025-11-29 015928.png  
│     ├── Screenshot 2025-11-29 015936.png  
│     ├── Screenshot 2025-11-29 015944.png  

## 🧹 ETL Pipeline (etl_cleaning.py)
The ETL script performs:
- Duplicate removal  
- Data type corrections  
- Datetime parsing  
- Fraud flag extraction  
- Feature creation:
  - Risk_Score  
  - Risk_Level  
  - Anomaly  
  - MonthName / MonthIndex  
  - High_Risk_Count  
- Export of fully cleaned dataset for BI analysis

## 📊 Power BI Dashboard – 4 Pages  
Here are the screenshots stored under /images uploaded to GitHub:

### 📍 Page 1 — Audit Overview
![Page 1](images/Screenshot%202025-11-29%20015830.png)

### 📍 Page 2 — Fraud & Anomaly Detection
![Page 2](images/Screenshot%202025-11-29%20015928.png)

### 📍 Page 3 — Risk Profiling
![Page 3](images/Screenshot%202025-11-29%20015936.png)

### 📍 Page 4 — Merchant Drill-Through Profile
![Page 4](images/Screenshot%202025-11-29%20015944.png)


## 🧩 Key Insights
- 91M+ total transaction value  
- 8K+ fraud transactions  
- Fraud dense in Grocery, Shopping POS, Entertainment  
- High risk patterns match anomaly + high z-score  
- Merchant-level drill-through reveals repeated offenders  

## 📥 Getting Started
Clone the repo:
git clone https://github.com/Gouse05/Credit-Card-Fraud-Analytics.git

Run ETL:
python etl_cleaning.py

Open in Power BI:
Import the CSV → Load PBIX → Explore dashboards.

## 👤 Author
**Gouse Pasha**  
GitHub: Gouse05

## ⭐ Support  
If you liked this project, please ⭐ the repository!
