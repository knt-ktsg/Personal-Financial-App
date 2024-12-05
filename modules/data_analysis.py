import pandas as pd


def analyze_spending(df):
    print("--- Total Spending by Category ---")
    total_spending = df.groupby("Category")["Amount"].sum()
    print(total_spending.to_string())


def calculate_monthly_spending(df):
    print("--- Average Monthly Spending ---")
    df['Date'] = pd.to_datetime(df['Date'])
    average_spending = df.groupby(df['Date'].dt.month)['Amount'].mean()
    average_spending.index.name = None
    print(average_spending.to_string())


def top_spending(df):
    print("--- Top Spending category ---")
    max_row = df[df.Amount == df.Amount.max()]
    category = max_row['Category'].to_string(index=None).replace(" ", "")
    max_amount = max_row['Amount'].to_string(index=None).replace(" ", "")
    print(f"{category} with {max_amount} total spending.")


