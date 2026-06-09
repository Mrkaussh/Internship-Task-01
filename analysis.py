"""
Internship Project: Retail Sales Data Analysis
Author: Data Science Intern
Description: This script imports, cleans, processes, and visualizes a raw retail dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a directory to save visualizations
os.makedirs('visualizations', exist_ok=True)

# ---------------------------------------------------------
# 1. Import and explore the dataset
# ---------------------------------------------------------
print("--- Importing Dataset ---")
# Load the dataset
df = pd.read_csv('raw_sales_data.csv')

# Display the first few rows to understand the structure
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset info (columns, data types, non-null counts)
print("\nDataset Info:")
df.info()

# ---------------------------------------------------------
# 2. Data Cleaning
# ---------------------------------------------------------
print("\n--- Data Cleaning ---")

# Step 2a: Handle missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# We will fill missing 'Quantity' with the median value
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

# We will fill missing 'Unit_Price' with the median value
df['Unit_Price'] = df['Unit_Price'].fillna(df['Unit_Price'].median())

# For 'Customer_Age', we can fill missing values with the mean age
df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].mean())

# Recalculate Total_Sales just in case there were missing values previously
df['Total_Sales'] = df['Quantity'] * df['Unit_Price']

# Step 2b: Handle Duplicates
# Check for duplicate rows
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows found: {duplicates}")

# Remove duplicates
df = df.drop_duplicates()
print("Duplicates removed.")

# Step 2c: Handle Outliers (Customer_Age)
# A typical second-year approach: anything above 100 years in Age is likely an error here.
# Let's cap the age at 90.
print("\nHandling outliers in 'Customer_Age'...")
df['Customer_Age'] = np.where(df['Customer_Age'] > 90, 90, df['Customer_Age'])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save the cleaned dataset
df.to_csv('cleaned_sales_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_sales_data.csv'.")

# ---------------------------------------------------------
# 3 & 4. Preprocessing and Visualization
# ---------------------------------------------------------
print("\n--- Generating Visualizations ---")

# Set the visualization style
sns.set_theme(style="whitegrid")

# Visualization 1: Bar Chart - Total Sales by Product Category
plt.figure(figsize=(10, 6))
sales_by_category = df.groupby('Product_Category')['Total_Sales'].sum().reset_index()
sns.barplot(data=sales_by_category, x='Product_Category', y='Total_Sales', palette='viridis')
plt.title('Total Sales by Product Category', fontsize=16)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.savefig('visualizations/bar_chart_sales_by_category.png')
plt.close()
print("Saved Bar Chart: visualizations/bar_chart_sales_by_category.png")

# Visualization 2: Histogram - Distribution of Customer Ages
plt.figure(figsize=(8, 5))
sns.histplot(df['Customer_Age'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Customer Ages', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.savefig('visualizations/histogram_age_distribution.png')
plt.close()
print("Saved Histogram: visualizations/histogram_age_distribution.png")

# Visualization 3: Scatter Plot - Quantity vs Total Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Quantity', y='Total_Sales', hue='Product_Category', palette='deep', alpha=0.7)
plt.title('Quantity vs Total Sales', fontsize=16)
plt.xlabel('Quantity Purchased', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.savefig('visualizations/scatter_quantity_vs_sales.png')
plt.close()
print("Saved Scatter Plot: visualizations/scatter_quantity_vs_sales.png")

# Visualization 4: Heatmap - Correlation Matrix
plt.figure(figsize=(8, 6))
# Select only numeric columns for correlation
numeric_cols = df.select_dtypes(include=[np.number])
corr_matrix = numeric_cols.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Numeric Features', fontsize=16)
plt.savefig('visualizations/heatmap_correlation.png')
plt.close()
print("Saved Heatmap: visualizations/heatmap_correlation.png")

print("\nAll tasks completed successfully!")
