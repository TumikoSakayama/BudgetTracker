from btracker import BudgetTracker
from category import Category
from transaction import Transaction

if __name__ == "__main__":
    
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
        elif option == '2':
            print("Here we add transactions")
        elif option == '3':
            print("We will calculate the total based on transactions")
        elif option == '4':
            print("Bye Bye!")
            break
        else:
            print("Wrong option retard")
            break