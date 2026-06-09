# Retail Sales Data Analysis Report
**Author:** Data Science Intern

## Overview
This project involves cleaning, processing, and analyzing a raw retail dataset to uncover meaningful insights about customer purchasing behavior.

## 1. Data Cleaning & Preprocessing
The raw dataset initially had **500 rows** and **9 columns**. The following data cleaning steps were performed using Pandas:
- **Missing Values:** Addressed missing values in the `Quantity`, `Unit_Price`, and `Customer_Age` columns. Missing numeric values were filled using median (for skewed distributions like sales/quantity) and mean (for age).
- **Duplicates:** Identified and removed 10 duplicate rows to ensure data integrity.
- **Outliers:** Handled an outlier in `Customer_Age` by capping unrealistic ages (e.g., > 100 years) to a reasonable maximum (90 years).

## 2. Key Insights and Visualizations
The cleaned data was visualized using **Matplotlib** and **Seaborn**.

### Insight 1: Total Sales by Product Category
> **Finding:** The Electronics category dominates the total sales volume due to their higher unit prices compared to other categories like Toys or Clothing.

![Total Sales by Product Category](file:///c:/Users/mkaus/Confidential/Internship%20Task/visualizations/bar_chart_sales_by_category.png)

### Insight 2: Customer Demographics
> **Finding:** The distribution of customer ages is roughly normal, centered around 35 years old. This suggests our primary demographic is young to middle-aged adults.

![Distribution of Customer Ages](file:///c:/Users/mkaus/Confidential/Internship%20Task/visualizations/histogram_age_distribution.png)

### Insight 3: Purchasing Behavior
> **Finding:** The scatter plot reveals that Total Sales increases linearly with Quantity, as expected. However, the slope varies by Product Category, indicating different average unit prices.

![Quantity vs Total Sales](file:///c:/Users/mkaus/Confidential/Internship%20Task/visualizations/scatter_quantity_vs_sales.png)

### Insight 4: Feature Correlation
> **Finding:** There is a strong positive correlation between `Quantity`, `Unit_Price`, and `Total_Sales`. `Customer_Age` does not show a significant linear correlation with spending habits in this dataset.

![Correlation Matrix](file:///c:/Users/mkaus/Confidential/Internship%20Task/visualizations/heatmap_correlation.png)

## Conclusion & Storytelling Summary
Our analysis of the retail data shows that our core customer base consists of adults in their mid-30s. While they purchase across all categories, certain high-value categories drive the bulk of our revenue. By ensuring high data quality—removing duplicates, handling missing entries, and addressing outliers—we were able to build reliable visual reports. These insights can help the marketing team tailor their campaigns towards the primary age demographic and focus promotions on the most profitable product lines.
