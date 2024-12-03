from modules import data_management

def main():
    df = None
    while True:
        choose_option = data_management.display_main_menu()
        if choose_option == "0":
            path = input("Please enter the path of the CSV file: ")
            df = data_management.import_csv(path)
            input("Press 'Enter' to return to the main menu...")
            print("")

        elif choose_option == "1":
            print("--- All Transactions ---")
            data_management.view_transactions(df)
            input("Press 'Enter' to return to the main menu...")
            print("")

        elif choose_option == "2":
            data_management.view_transactions_date(df)
            input("Press 'Enter' to return to the main menu...")
            print("")

        elif choose_option == "11":
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break

        else:
            print("Invalid input! Please enter 1 ~ 11.")


main()
