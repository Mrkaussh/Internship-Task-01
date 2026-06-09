import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of rows
n = 500

# Generate data
transaction_ids = [f"TXN_{i:04d}" for i in range(1, n + 1)]

# Dates within the last year
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(n)]

categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Toys']
product_categories = random.choices(categories, weights=[30, 25, 20, 15, 10], k=n)

quantities = np.random.randint(1, 10, size=n).astype(float)
unit_prices = np.round(np.random.uniform(10.0, 500.0, size=n), 2)

# Introduce some missing values
for _ in range(25):
    quantities[random.randint(0, n - 1)] = np.nan
for _ in range(20):
    unit_prices[random.randint(0, n - 1)] = np.nan

# Calculate total sales where possible
total_sales = quantities * unit_prices

# Customer demographics
ages = np.random.normal(loc=35, scale=12, size=n)
ages = np.clip(ages, 18, 70).astype(float)
# Add some outliers to age
for _ in range(5):
    ages[random.randint(0, n - 1)] = random.randint(100, 120)
# Add missing values to age
for _ in range(30):
    ages[random.randint(0, n - 1)] = np.nan

genders = random.choices(['Male', 'Female', 'Other'], weights=[48, 48, 4], k=n)

locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
store_locations = random.choices(locations, k=n)

# Create DataFrame
df = pd.DataFrame({
    'Transaction_ID': transaction_ids,
    'Date': dates,
    'Product_Category': product_categories,
    'Quantity': quantities,
    'Unit_Price': unit_prices,
    'Total_Sales': total_sales,
    'Customer_Age': ages,
    'Customer_Gender': genders,
    'Store_Location': store_locations
})

# Add some duplicates
duplicates = df.sample(10, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv('raw_sales_data.csv', index=False)
print("raw_sales_data.csv generated successfully.")
