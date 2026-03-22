import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

# Show basic info
print(df.head())
print(df.columns)
print(df.info())

# Total Sales
print("Total Sales:", df['Sales'].sum())

# Top 5 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head()

top_products.plot(kind="bar")
plt.title("Top 5 Products")
plt.xlabel("Product Name")
plt.ylabel("Sales")
plt.show()


# Sales by Region
df.groupby('Region')['Sales'].sum().plot(kind='bar')

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()


# Monthly Sales Trend
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

monthly_sales = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

print(monthly_sales)

monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
