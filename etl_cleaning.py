import pandas as pd
import numpy as np

# Load your external dataset
df = pd.read_csv("fraudTrain.csv")

# Remove unneeded index column
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Convert transaction datetime
df["trans_date_trans_time"] = pd.to_datetime(df["trans_date_trans_time"])

# Rename important fields
df.rename(columns={
    "trans_date_trans_time": "TransactionDate",
    "amt": "Amount",
    "merchant": "Merchant",
    "category": "Category",
    "is_fraud": "FraudFlag"
}, inplace=True)

# Create Month column
df["Month"] = df["TransactionDate"].dt.to_period("M").astype(str)

# Add Age (optional for audit analysis)
df["dob"] = pd.to_datetime(df["dob"], errors="coerce")
df["Age"] = df["TransactionDate"].dt.year - df["dob"].dt.year

# Basic data cleaning
df = df[df["Amount"] > 0]              # only positive transactions
df["Category"] = df["Category"].astype(str).str.title()

# Anomaly detection using Z-score
df["zscore"] = (df["Amount"] - df["Amount"].mean()) / df["Amount"].std()
df["Anomaly"] = df["zscore"].abs() > 3

# Risk Score Logic
def risk(row):
    if row["FraudFlag"] == 1:
        return "High"
    if row["Anomaly"]:
        return "Medium"
    return "Low"

df["Risk_Level"] = df.apply(risk, axis=1)

risk_map = {"Low": 1, "Medium": 2, "High": 3}
df["Risk_Score"] = df["Risk_Level"].map(risk_map)

# Save cleaned dataset
df.to_csv("transactions_cleaned.csv", index=False)

print("ETL Completed — Cleaned data saved as transactions_cleaned.csv")
