import pandas as pd

#Load dataset
df = pd.read_csv("train.csv")

# Show first rows
print(df.head())
print(df.columns)
print(df.info())

# Total Sales
print("Total Sales:", df['Sales'].sum())

# Sales by Region
print(df.groupby('Region')['Sales'].sum())


# Monthly Trend Sales
df['Order Date']= pd.to_datetime(df['Order Date'],dayfirst=True)
monthly_sales = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

import matplotlib.pyplot as plt


monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

