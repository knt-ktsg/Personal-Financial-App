import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def set_monthly_income():
    while True:
        try:
            set_income = float(input("Enter your total monthly income: "))
            if set_income >= 0:
                print(f"Your monthly income is set to: ${set_income}")
                break
            else:
                print("The income has to be positive number.")
                continue

        except ValueError:
            print("Invalid input! Please enter the number.")
            continue


def set_category_budget():
    food_budget = 0
    rent_budget = 0
    utilities_budget = 0
    transport_budget = 0

    while True:
        try:
            food_budget = float(input("Enter your budget for Food: "))
            if food_budget >= 0:
                break
            else:
                print("The budget has to be positive number.")
                continue

        except ValueError:
            print("Invalid input! Please enter the number.")
            continue

    while True:
        try:
            rent_budget = float(input("Enter your budget for Rent: "))
            if rent_budget >= 0:
                break
            else:
                print("The budget has to be positive number.")
                continue

        except ValueError:
            print("Invalid input! Please enter the number.")
            continue

    while True:
        try:
            utilities_budget = float(input("Enter your budget for Utilities: "))
            if utilities_budget >= 0:
                break
            else:
                print("The budget has to be positive number.")
                continue

        except ValueError:
            print("Invalid input! Please enter the number.")
            continue

    while True:
        try:
            transport_budget = float(input("Enter your budget for Transport: "))
            if transport_budget >= 0:
                break
            else:
                print("The budget has to be positive number.")
                continue

        except ValueError:
            print("Invalid input! Please enter the number.")
            continue

    print("")
    print("Your budgets have been set:")
    print(f"- Food: ${food_budget}")
    print(f"- Rent: ${rent_budget}")
    print(f"- Utilities: ${utilities_budget}")
    print(f"- Transport: ${transport_budget}")


# def check_budget_status():


# Visualization
def monthly_income_spending(df):
    df['Date'] = pd.to_datetime(df['Date'])
    monthly = df.groupby([df['Date'].dt.month, "Category"])['Amount'].sum().unstack(fill_value=0).reset_index()
    monthly = monthly.melt(id_vars=['Date'], var_name='Category', value_name='Amount')
    monthly_income = monthly[monthly["Category"] == "Income"]
    monthly_spending = monthly[monthly["Category"] != "Income"].groupby("Date")["Amount"].sum()
    monthly_spending = pd.DataFrame(monthly_spending).reset_index()
    sns.lineplot(data=monthly_income, x="Date", y="Amount", label="Total Income")
    sns.lineplot(data=monthly_spending, x="Date", y="Amount", label="Total Spending")
    plt.title("Monthly Income vs Spending")
    plt.xlabel("Months")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()
