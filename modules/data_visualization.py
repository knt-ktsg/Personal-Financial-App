import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def select_visualization(df):
    print("\n1. Monthly Spending Category\
          \n2. Spending by Category\
          \n3. Percentage Distribution\
          \n4. Spending Trend\
          \n5. Category Spending vs Budget")
    selection = input("Which graph do you want to see? Please select 1~5: ")
    return selection


def visualize_spending_trend(df):
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_spending = df.groupby([df['Date'].dt.month, "Category"])['Amount'].sum().unstack(fill_value=0).reset_index()
    monthly_spending = monthly_spending.melt(id_vars=['Date'], var_name='Category', value_name='Amount')
    monthly_spending = monthly_spending[monthly_spending["Category"] != "Income"]
    sns.lineplot(data=monthly_spending, x="Date", y="Amount", hue="Category")
    plt.title("Monthly Spending Trend")
    plt.xlabel("Months")
    plt.ylabel("Values")
    plt.legend(title="Category")
    plt.xticks(ticks=range(1, 13))
    plt.tight_layout()
    plt.show()


def visualize_spending_category(df):
    spending_category = df.groupby("Category")['Amount'].sum()
    spending_category = spending_category.drop("Income").sort_values(ascending=False)
    color = ["dodgerblue", "red", "limegreen", "orange"]
    plt.bar(spending_category.index, spending_category.values, color=color)
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Values")
    plt.tight_layout()
    plt.show()


def visualize_percentage(df):
    spending_category = df.groupby("Category")['Amount'].sum()
    spending_category = spending_category.drop("Income").sort_values(ascending=False)
    df_percentage = pd.DataFrame(data={'category': spending_category.index, 'spending': spending_category.values})
    labels = df_percentage['category']
    plt.pie(df_percentage['spending'], counterclock=False, startangle=90, autopct='%1.0f%%', labels=None)
    plt.title("Percentage Distribution")
    plt.legend(labels, loc="center")
    plt.tight_layout()
    plt.show()

# Extended features
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

def category_spending_budget(check_budget, categories):
    if not categories:
        print("Please set the category budget first (option 10).")

    else:
        while True:
            try:
                month = int(input("Choose the month:"))
                if month in range(1, 13):
                    break
                else:
                    print("Invalid input! Please enter the corrct month from 1 to 12.")

            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

        index = month
        result = check_budget.index
        spending_month = list(pd.Index(result))

        name = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

        if index in spending_month:
            spending = check_budget.loc[[index]].iloc[0]

            plt.bar(spending.index, spending.values, label="Spending", align="edge", width=-0.4)
            plt.bar(categories.keys(), categories.values(), label="Budget", align="edge", width=0.4)
            for month_name, month_num in name.items():
                if index == month_num:
                    plt.title(f"Actual Spending vs Budget in {month_name}")
            plt.xlabel("Categories")
            plt.ylabel("Amount")
            plt.legend()
            plt.tight_layout()
            plt.show()

        else:
            print("There are no transactions this month.")
