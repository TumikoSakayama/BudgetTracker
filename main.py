import os
import csv
from btracker import BudgetTracker
from category import Category
from transaction import Transaction

def load_balance(filename):
    if not filename.endswith('.csv'):
        filename += '.csv'

    if not os.path.exists(filename):
        print("File not found!")
        return None

    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            if not rows or rows[0][0] != 'INITIAL_BALANCE':
                print("Error: Invalid csv format")
                return None

            initial_balance = float(rows[0][1])

            tracker = BudgetTracker(initial_balance)

            for row in rows[1:]:
                if len(row) < 4: continue

                cat_name, amount, trans_name, trans_type = row

                try:
                    tracker.add_category(cat_name)
                except ValueError:
                    pass

                try:
                    tracker.add_category(cat_name, float(amount), trans_name, trans_type)
                except ValueError as e:
                    print(f"Skipping invalid transaction: {e}")

            print(f"Loaded {len(rows)-1} transaction from {filename}.")
            return tracker

    except Exception as e:
        print(f"Error loading file: {e}")
        return None

if __name__ == "__main__":

    print("BUDGET TRACKER SETUP")
    first_choice = input("1. Create New Budget\n2. Load Existing Budget\nSelect:")

    tracker = None

    if first_choice == '2':
        fname = input("Enter the file name to load: ")
        tracker = load_balance(fname)

    if tracker is None:
        if first_choice == '2':
            print("Creating a new budget")
        try:
            bal_start = float(input("Enter initial balance of the month: "))
            tracker = BudgetTracker(bal_start)
        except ValueError:
            print("Invalid number. Starting with 0")
            tracker = BudgetTracker(0)
    
    while True:
        print("\n======Welcome to the Budget Tracker======\n")
        print("1. Add a new category")
        print("2. Add a new transaction")
        print("3. Show Total Balance")
        print("4. Exit the menu")
        option = input("Input your option: ")

        if option == '1':
            category_name = input("Enter the name of the new category: ")
            try:
                tracker.add_category(category_name)
                print(f"Category '{category_name}' added successfully.")
            except ValueError as e:
                print(e)
            print("===============================================\n")

        elif option == '2':
            try:
                amount = float(input("Enter the amount: "))
                cat_name = input("Category name: ")
                trans_name = input("Transaction completed: ")
                trans_type = input("Type (income/expense): ")

                tracker.add_transaction(cat_name, amount, trans_name, trans_type)
                print(f"Transaction '{trans_name}' added successfully to category '{cat_name}'.")
            except ValueError as e:
                print(f"Error: {e}")
            print("===============================================\n")

        elif option == '3':
            print("\n===== BALANCE REPORT =====\n")
            print(tracker.view_balance())
            print("=============================\n")

        elif option == '4':
            save = input("Do you want to save the changes (y/n): ")
            if save.lower() == 'y':
                save_name = input("Enter filename to save: ")
                tracker.save_to_csv(save_name)
            print("Bye bye!")
            break

        else:
            print("Wrong option retard")
            break