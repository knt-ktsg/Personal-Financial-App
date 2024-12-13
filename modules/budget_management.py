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
    global categories
    categories = {"Food": 0, "Rent": 0, "Utilities": 0, "Transport": 0}
    for category in categories:
        while True:
            try:
                budget = float(input(f"Enter your budget for {category}: "))
                if budget >= 0:
                    categories[category] = budget
                    break
                else:
                    print("The budget has to be positive number.")

            except ValueError:
                print("Invalid input! Please enter a valid number.")

    print("")
    print("Your budgets have been set:")
    for category, amount in categories.items():
        print(f"- {category}: ${amount}")

    return categories


def check_budget_status(df, categories):
    warning = ["(Exact: Budget met!)", "(Alert: Exceeded budget!)", "(Warning: Close to budget!)"]
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
        for category, budget in categories.items():
            amount = spending.get(category)
            if amount == budget:
                message = warning[0]
            elif amount > budget:
                message = warning[1]
            elif amount >= budget * 0.9:
                message = warning[2]
            else:
                message = ""

            print(f"- {category}: ${amount} / ${budget} {message}")

    else:
        for month_name, month_num in name.items():
            if month == month_num:
                print(f"There is no transaction in {month_name}.")
                break