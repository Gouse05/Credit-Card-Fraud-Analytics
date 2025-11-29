\# Credit Card Fraud \& Risk Analytics Dashboard



An end-to-end ETL + Anomaly Detection + Power BI Dashboard project using Python \& Power BI.  

Processes real credit card transactions, detects fraud and anomalies, and provides audit-ready insights.



\## ⚙️ Tech Stack

Python (Pandas, NumPy), Power BI (DAX, Drill-through), Z-score Anomaly Detection, Git \& GitHub



\## 🔄 Python ETL Pipeline

\- Loaded raw dataset (fraudTrain.csv)

\- Cleaned missing and inconsistent data

\- Converted timestamp to TransactionDate

\- Added MonthName, MonthIndex, Age, and other engineered features

\- Applied Z-score anomaly detection (zscore column)

\- Created Risk\_Score and Risk\_Level (Low/Medium/High)

\- Exported final cleaned dataset → transactions\_cleaned.csv



\## 📊 Power BI Dashboard Pages

1️⃣ Audit Overview  

• KPIs (Total Amount, Transaction Count, Fraud Count, High-Risk Count)  

• Category Spend Bar Chart  

• Monthly Trend Line Chart  

• Complete Audit Table with risk levels and anomalies  



2️⃣ Fraud \& Anomaly Detection  

• Fraud-only table  

• Fraud by Category bar chart  

• Amount vs Z-score scatter plot for anomaly visualization  



3️⃣ Risk Profiling  

• Risk Level Donut Chart  

• Risk Score Histogram  

• High-Risk Merchant Table  



4️⃣ Merchant Drill-Through Profile  

• Merchant-specific KPIs  

• Total amount, fraud count, average risk score  

• Full transaction ledger  

• Right-click drill-through enabled for auditors  



\## 🖼️ Dashboard Screenshots

Upload your screenshots into a folder named \*\*images/\*\* in your repo, then they will automatically appear.



\### Page 1 – Audit Overview

!\[Page 1](images/page1.png)



\### Page 2 – Fraud \& Anomaly Detection

!\[Page 2](images/page2.png)



\### Page 3 – Risk Profiling

!\[Page 3](images/page3.png)



\### Page 4 – Merchant Drill-Through

!\[Page 4](images/page4.png)



\## 📂 Folder Structure

credit-card-fraud-analytics/  

│── etl\_cleaning.py  

│── transactions\_cleaned.csv  

│── powerbi\_dashboard.pbix (optional)  

│── images/  

│     ├── page1.png  

│     ├── page2.png  

│     ├── page3.png  

│     └── page4.png  

│── README.md  



\## ⭐ Key DAX Measures

Total Amount = SUM('transactions\_cleaned'\[Amount])  

Transaction Count = COUNTROWS('transactions\_cleaned')  

Fraud Count = SUM('transactions\_cleaned'\[FraudFlag])  

High Risk Count = CALCULATE(COUNTROWS('transactions\_cleaned'), 'transactions\_cleaned'\[Risk\_Level] = "High")  

Avg Risk Score = AVERAGE('transactions\_cleaned'\[Risk\_Score])  



\## 🚀 How to Run

1\. Run ETL script: python etl\_cleaning.py  

2\. Load transactions\_cleaned.csv into Power BI  

3\. Open .pbix dashboard  

4\. Explore insights using slicers, filters, and drill-through  



\## 🙌 Author

Sheik Gouse Pasha



