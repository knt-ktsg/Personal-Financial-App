import pandas as pd
from datetime import datetime

def display_main_menu():
    print("=== Personal Finance Tracker ===")
    print("0. Import a CSV file\
          \n1. View All Transactions\
          \n2. View Transactions by Date Range\
          \n3. Add a Transaction\
          \n4. Edit a Transaction\
          \n5. Delete a Transaction\
          \n6. Analyze Spending by Category\
          \n7. Calculate Average Monthly Spending\
          \n8. Show Top Spending Category\
          \n9. Visualize Monthly Spending Trend\
          \n10. Save Transactions to CSV\
          \n11. Exit")
    return input("Choose an option (0-11): ")


def import_csv(path):
    try:
        df = pd.read_csv(path)
        print("The DataFrame is successfully imported.")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def view_transactions(df):
    if df is None:
        print("There is no data to display.")
    elif df.empty:
        print("The Dataframe is empty.")
    else:
        return print(df)


def view_transactions_date(df):
    if df is None or df.empty:
        print("There is no data to display.")
        return

    def validate_format(date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    while True:
        start = input("Enter the start date (YYYY-MM-DD): ")
        if validate_format(start):
            break
        else:
            print("Invalid input!")
            continue

    while True:
        end = input("Enter the end date (YYYY-MM-DD): ")
        if validate_format(end):
            break
        else:
            print("Invalid input!")
            continue

    print(f"\n--- Transactions from {start} to {end} ---")
    date_range = df[(df['Date'] >= start) & (df['Date'] <= end)]

    if date_range.empty:
        print("No transactions found in this date range.")
    else:
        return print(date_range)
