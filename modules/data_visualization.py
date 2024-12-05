import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualize_spending_trend(df):
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_spending = df.groupby([df['Date'].dt.month, "Category"])['Amount'].sum().unstack(fill_value=0).reset_index()
    monthly_spending = monthly_spending.melt(id_vars=['Date'], var_name='Category', value_name='Amount')
    sns.lineplot(data=monthly_spending, x="Date", y="Amount", hue="Category")
    plt.title("Visualize Monthly Spending")
    plt.xlabel("Months")
    plt.ylabel("Values")
    plt.legend(title="Category")
    plt.xticks(ticks=range(1, 13))
    plt.tight_layout()
    plt.show()