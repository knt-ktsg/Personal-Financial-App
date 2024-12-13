import pandas as pd


def set_monthly_income():
    while True:
        try:
            set_income = float(input("Enter your total monthly income: "))
            if set_income >= 0:
                print(f"Your monthly income is set to: ${set_income}")
                print("")
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
    print("")


def check_budget_status(df):
    month = None
    while True:
        try:
            month = int(input("Enter the month you want to compare actual spending and budget: "))
            if month in range(1, 13):
                break
            else:
                print("Invalid input! Please enter the corrct month from 1 to 12.")

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

    df = df[df['Category'] != "Income"]
    df['Date'] = pd.to_datetime(df['Date'])
    check_budget = df.groupby([df['Date'].dt.month, "Category"])['Amount'].sum().unstack(
        fill_value=0).reset_index().rename(columns={'Date': 'Month'}).set_index("Month")

    name = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
            "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    index = month
    result = check_budget.index
    spending_month = list(pd.Index(result))

    if index in spending_month:
        spending = check_budget.loc[[index]]
        print("")
        print("--- Budget Status ---")
        print(f"Month: {spending.index[0]}")
        print(f"- Food: ${spending.Food.iloc[0]}")
        print(f"- Rent: ${spending.Rent.iloc[0]}")
        print(f"- Utilities: ${spending.Utilities.iloc[0]}")
        print(f"- Transport: ${spending.Transport.iloc[0]}")
        print("")

    else:
        for month_name, month_num in name.items():
            if month == month_num:
                print(f"There is no transaction in {month_name}.")
                break