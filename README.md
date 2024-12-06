# Personal-Financial-App

## Overview
The Personal Finance Tracker App is an application that helps users manage and analyze their spending habits. 
Users can import a CSV file containing transaction data, perform operations like viewing, adding,
editing, and deleting transactions, and analyze spending patterns. 
The app also includes data visualization capabilities, displaying monthly spending trends and top spending categories. 
This application is built using Python and uses libraries like Pandas for data handling, and Matplotlib, and Seaborn for visualization.

## Features
**1. File import Functionality**
* Import a CSV file containing your transaction data. This file must contain columns such as Date, Category, Description, Amount, and Type.

**2. Data Management**
* **View Transactions by Date Range:** Filter and display transactions within a
specified date range.
* **Add a Transaction:** Add a new transaction with details like date, category,
description, and amount.
* **Edit a Transaction:** Modify details of an existing transaction (date,
category, description, amount).
* **Delete a Transaction:** Remove a specific transaction by its index.

**3. Spending Analysis**
* **Analyze Spending by Category:** Display total spending for each category.
* **Calculate Average Monthly Spending:** Show average spending per month.
* **Show Top Spending Category:** Identify the category with the highest total spending.

**4. Data Visualization**
* **Monthly Spending Trend:** Visualize spending trends over time using a line
chart. 
* **Spending by Category:** Create a bar chart showing total spending by category.
* **Percentage Distribution:** Generate a pie chart representing the distribution of spending across categories.

**5. Save Transactions to CSV:** 
* Save the updated list of transactions to a CSV file, maintaining a record of
financial data.