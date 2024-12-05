import pandas as pd
from datetime import datetime
import re


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
        print(df)


def validate_format(date):
    correct_format = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(correct_format, date):
        return False

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def view_transactions_date(df):
    if df is None or df.empty:
        print("There is no data to display.")
        return

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
        print(date_range)


def add_transactions(df):
    if df is None:
        print("There is no data to display.")
        return

    new = {}

    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if validate_format(date):
            new["Date"] = date
            break
        else:
            print("Invalid input!")
            continue

    while True:
        category = str(input("Enter the category: "))
        if category.isalpha():
            new["Category"] = category
            break
        else:
            print("Invalid input! Please enter an appropriate category.")
            continue

    while True:
        des = str(input("Enter a description: "))
        if des.isalpha():
            new["Description"] = des
            break
        else:
            print("Invalid input! Please enter an appropriate description.")
            continue

    while True:
        try:
            amount = float(input("Enter the amount: "))
            formatted_amount = round(amount, 2)
            new["Amount"] = formatted_amount
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

    while True:
        types = str(input("Enter a type: "))
        if types.isalpha():
            new["Type"] = types
            break
        else:
            print("Invalid input! Please enter an appropriate Type.")
            continue

    add_df = pd.DataFrame([new])
    df = pd.concat([df, add_df])
    df = df.sort_values(by=['Date'], ignore_index=True)
    print("Transaction added successfully!")
    return df
    # input("Do you want to add more transactions? (yes/no)")


def edit_transaction(df):
    if df is None:
        print("There is no data to display.")
        return

    edit_index = None

    while True:
        try:
            edit_index = int(input("Enter the index of the transaction to edit: "))
            if edit_index < 0 or edit_index >= len(df):
                raise IndexError
            print("")
            print("Current Transaction Details:")
            print(df.iloc[edit_index])
            print("")
            break

        except IndexError:
            print("Invalid input! Please enter valid index.")
            continue

        except ValueError:
            print("Invalid input!")
            continue

    while True:
        edit_date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current: ")
        if validate_format(edit_date):
            df.loc[edit_index, "Date"] = edit_date
            break
        elif edit_date == "":
            break
        else:
            print("Invalid input! Please enter valid date.")
            continue

    while True:
        edit_category = str(input("Enter new category or press Enter to keep current: "))
        if edit_category.isalpha():
            df.loc[edit_index, "Category"] = edit_category
            break
        elif edit_category == "":
            break
        else:
            print("Invalid input! Please enter an appropriate category.")
            continue

    while True:
        edit_des = str(input("Enter new description or press Enter to keep current: "))
        if edit_des.isalpha():
            df.loc[edit_index, "Description"] = edit_des
            break
        elif edit_des == "":
            break
        else:
            print("Invalid input! Please enter an appropriate description.")
            continue

    while True:
        edit_amount = input("Enter new amount or press Enter to keep current: ")
        if edit_amount == "":
            break
        try:
            edit_amount = float(edit_amount)
            formatted_amount = round(edit_amount, 2)
            df.loc[edit_index, "Amount"] = formatted_amount
            break

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

    while True:
        edit_types = str(input("Enter new type or press Enter to keep current: "))
        if edit_types.isalpha():
            df.loc[edit_index, "Type"] = edit_types
            break
        elif edit_types == "":
            break
        else:
            print("Invalid input! Please enter an appropriate Type.")
            continue

    print("Transaction updated successfully!")
    df = df.sort_values(by=['Date'], ignore_index=True)
    return df


def delete_transaction(df):
    while True:
        try:
            index = int(input("Enter the index of the transaction to delete: "))
            df = df.drop(index).reset_index(drop=True)
            print("Transactions deleted successfully!")
            return df

        except KeyError:
            print("Invalid input! Please enter valid ind