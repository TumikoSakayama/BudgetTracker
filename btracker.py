from category import Category as category

class BudgetTracker:
    def __init__(self, balance):
        self.categories = []
        self.balance = balance

    def add_category(self, category_name):
        category_name = category(category_name)
        self.categories.append(category_name)
        return category_name
    
    def add_transaction(self, category, amount, transaction_name, transaction_type):
        category.add_transaction(amount, transaction_name, transaction_type)
    
    def view_balance(self):
        for category in self.categories:
            category_balance = category.calculate_balance()
            print(f"Category: {category.name}, Balance: ${category_balance}")
            self.balance += category_balance
        print(f"Total Balance: ${self.balance}")