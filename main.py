from btracker import BudgetTracker
from category import Category
from transaction import Transaction

if __name__ == "__main__":
    # Initialize Budget Tracker with a starting balance of $1000
    budget_tracker = BudgetTracker(1000)

    # Add categories
    food_category = budget_tracker.add_category("Food")
    entertainment_category = budget_tracker.add_category("Entertainment")

    # Add transactions to Food category
    budget_tracker.add_transaction(food_category, 150, "Groceries", "expense")
    budget_tracker.add_transaction(food_category, 50, "Dining Out", "expense")
    budget_tracker.add_transaction(food_category, 200, "Salary Bonus", "income")

    # Add transactions to Entertainment category
    budget_tracker.add_transaction(entertainment_category, 100, "Concert Ticket", "expense")
    budget_tracker.add_transaction(entertainment_category, 300, "Freelance Project", "income")

    # View balances
    budget_tracker.view_balance()