# :chart_with_upwards_trend: Personal Finance Tracker App

![Images](https://images.pexels.com/photos/6694543/pexels-photo-6694543.jpeg?auto=compress&cs=tinysrgb&w=1200)

## :books: Description
The Personal Finance Tracker App is an application that helps users manage and analyze their spending habits. 
Users can import a CSV file containing transaction data, perform operations like viewing, adding,
editing, and deleting transactions, and analyze spending patterns. 
The app also includes data visualization capabilities, displaying monthly spending trends, top spending categories, and comparing monthly income and spending.
This application is built with Python and uses libraries like Pandas for data handling, Matplotlib, and Seaborn for visualization.

## :clapper: Demo

You can view the demo video by clicking the link below:

[Watch the Demo Video](https://drive.google.com/file/d/1sGFCOPUqPhGjhZXtTi239M5AiwsP__kn/view?usp=sharing)


## :wrench: Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:knt-ktsg/Personal-Financial-App.git

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
## :computer: Usage
1. Run the following command to start the application:
   ```bash
   python main.py
   
## :file_folder: Example CSV File
Here is an example of the CSV file format used to track your expenses and income. This file includes 5 rows of data:

| Date       | Category | Description           | Amount |
|------------|----------|-----------------------|--------|
| 2024-01-01 | Food     | Grocery shopping      | 50.00  |
| 2024-01-05 | Rent     | Monthly rent payment  | 900.00 |
| 2024-01-07 | Utilities | Electricity bill      | 75.00  |
| 2024-01-10 | Transport | Public transport pass | 40.00  |
| 2024-01-15 | Income   | Freelance Work        | 30.00  |

### Columns:
- **Date**: The date when the transaction occurred (in `YYYY-MM-DD` format).
- **Category**: The type of the transaction (e.g., Food, Rent, Utilities).
- **Description**: A brief description of the transaction (e.g., "Grocery shopping").
- **Amount**: The amount spent or earned (your preferred currency).

## :gear: Features
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

**4. Budget Management**
* **Manage Income:** Enter income details to compare with expenses and understand your financial balance. 
* **Set Budget:** Set a overall monthly budget for each category. (Food, Rent, Utilities, Transport)
* **Alert with a Message:** Compare spending against the budget, and alert the user if spending is close to, exceeds or matches the budget perfectly.
* **Provide Suggestions:** Provide suggestions based on the analysis of spending patterns.

**5. Data Visualization**
* **Monthly Spending Trend:** Visualize spending trends over time using a line
chart. 
* **Spending by Category:** Visualize total spending by category using a bar chart.
* **Percentage Distribution:** Generate a pie chart to represent the distribution of spending across categories.
* **Spending Trends:** Generate a line chart to compare monthly income and total spending.
* **Category Spending vs Budget:** Display category-wise spending compared to the set budget using a bar chart.
* **Income and Expense Distribution:** Visualize the distribution of income and expenses using a pie chart for clear allocation insight.


**6. Save Transactions to CSV:** 
* Save the updated list of transactions to a CSV file, maintaining a record of
financial data.

## :lock: License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/knt-ktsg/Personal-Financial-App/blob/main/LICENSE) file for details.

## :envelope: Contact
Maintainer: [Kento Kitasuga](mailto:hokutonokento0706@gmail.com)