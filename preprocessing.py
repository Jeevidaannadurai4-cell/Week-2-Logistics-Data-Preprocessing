import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("logistics_dataset.csv")

print("Original shape:", df.shape)
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

numeric_cols = ["Distance_km", "Weight_kg", "Shipping_Cost", "Delivery_Time_days"]
categorical_cols = ["Shipping_Mode", "Warehouse", "Delivery_Status"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    df[col] = df[col].astype("string").str.strip().str.title()
    df[col] = df[col].fillna(df[col].mode()[0])

# IQR-based outlier treatment
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df[col] = df[col].clip(lower, upper)

# Min-Max normalization
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

df.to_csv("cleaned_logistics_dataset.csv", index=False)
print("Preprocessing completed successfully.")
