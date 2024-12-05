from modules import data_management
from modules import data_analysis

def main():
    df = None
    while True:
        choose_option = data_management.display_main_menu()
        if choose_option == "0":
            path = input("Please enter the path of the CSV file: ")
            df = data_management.import_csv(path)

        elif choose_option == "1":
            print("--- All Transactions ---")
            data_management.view_transactions(df)

        elif choose_option == "2":
            data_management.view_transactions_date(df)
            input("Press 'Enter' to return to the main menu...")
            print("")

        elif choose_option == "3":
            df = data_management.add_transactions(df)

        elif choose_option == "4":
            df = data_management.edit_transaction(df)

        elif choose_option == "5":
            df = data_management.delete_transaction(df)

        elif choose_option == "6":
            data_analysis.analyze_spending(df)

        elif choose_option == "7":
            data_analysis.calculate_monthly_spending(df)

        elif choose_option == "8":
            data_analysis.top_spending(df)

        elif choose_option == "11":
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break

        else:
            print("Invalid input! Please enter 1 ~ 11.")

        input("Press 'Enter' to return to the main menu...")
        print("")


main()

"/Users/kento/Desktop/Personal-Financial-App/sampledata.csv"