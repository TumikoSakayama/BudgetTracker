from btracker import BudgetTracker
from category import Category
from transaction import Transaction

if __name__ == "__main__":

    tracker = BudgetTracker(0)
    
    while True:
        print("Welcome to the Budget Tracker (terminal version)")
        print("================================================")
        print("Please select the task that you want to complete (1-3)")
        print("1. Add a new category")
        print("2. Add a new money movement")
        print("3. Show Total Balance")
        print("4. Exit the menu")
        option = input("Input your option: ")

        if option == '1':
            print("Here we will add categories to the tracker")
            category_name = input("Enter the name of the new category: ").capitalize()
            tracker.add_category(category_name.capitalize())
            print(f"Category '{category_name}' added successfully.")
            print("===============================================")
            print(tracker)
        elif option == '2':
            print("Here we add transactions")
            amount = int(input("Enter the amount: "))
            category_name = input("Enter the category name: ").capitalize()
            if not category_name in [cat.name for cat in tracker.categories]:
                print(f"Category '{category_name}' does not exist. Please add it first.")
                continue
            transaction_name = input("Enter the transaction name: ")
            transaction_type = input("Enter the transaction type (income/expense): ")
            category = next(cat for cat in tracker.categories if cat.name == category_name)
            tracker.add_transaction(category, amount, transaction_name, transaction_type)
            print(f"Transaction '{transaction_name}' added successfully to category '{category_name}'.")
            print("===============================================")
            print(tracker)
        elif option == '3':
            print("We will calculate the total based on transactions")
            tracker.view_balance()
            print("===============================================")
        elif option == '4':
            print("Bye Bye!")
            break
        else:
            print("Wrong option retard")
            break