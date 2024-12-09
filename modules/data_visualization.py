import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def select_visualization(df):
    print("1. Monthly Spending Category\
          \n2. Spending by Category\
          \n3. Percentage Distribution\
          \n4. Spending Trend")
    selection = input("Which graph do you want to see? Please select 1~3: ")
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
