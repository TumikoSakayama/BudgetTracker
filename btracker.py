from category import Category as category

class BudgetTracker:
    def __init__(self, balance):
        self.categories = []
        self.balance = balance

    def add_category(self, name):
        category_name = category(name)
        self.categories.append(category_name)
        return category_name
    
    def add_transaction(self, category, amount, transaction_name, transaction_type):
        category.add_transaction(amount, transaction_name, transaction_type)
    
    def view_balance(self):
        total = self.balance  # This is now just your "Starting Cash"
        for category in self.categories:
            cat_bal = category.calculate_balance()
            print(f"Category: {category.name}, Balance: ${cat_bal}")
            total += cat_bal
        print(f"Total Portfolio Balance: ${total}")

    def __str__(self):
        current_total = self.balance
        for category in self.categories:
            current_total += category.calculate_balance()

        if self.categories:
            category_list = ', '.join([str(cat.name) for cat in self.categories])
        else:
            category_list = 'No categories added yet.'
        return f"BudgetTracker(Balance: ${current_total}, Categories: {category_list})"