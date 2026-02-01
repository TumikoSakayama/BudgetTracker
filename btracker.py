from category import Category

class BudgetTracker:
    def __init__(self, balance):
        self.categories = []
        self.balance = balance

    def add_category(self, name):

        for cat in self.categories:
            if cat.name == name:
                raise ValueError(f"Category {name} already exists.\n")
        
        category_name = Category(name)
        self.categories.append(category_name)
        return category_name
    
    def add_transaction(self, cat_name, amount, transaction_name, transaction_type):
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("The amount must be a number.\n")
        
        if amount <= 0:
            raise ValueError("The amount must be more than 0.\n")

        if hasattr(cat_name, 'name'):
            cat_name = cat_name.name

        cat_name = str(cat_name)

        cat_target = None
        for cat in self.categories:
            if cat.name.lower() == cat_name.lower():
                cat_target = cat
                break

        if not cat_target:
            raise ValueError(f"Category {cat_name} not found.\n")

        try:
            cat_target.add_transaction(amount, transaction_name, transaction_type)
        except ValueError as e:
            raise ValueError(f"Transaction was not added: {e}\n")
    
    def view_balance(self):
        total = self.balance
        summary = []

        for category in self.categories:
            cat_bal = category.calculate_balance()
            summary.append(f"Category: {category.name}, Balance: ${cat_bal:.2f}")
            total += cat_bal

        result = "\n".join(summary)
        result += f"\nTotal Balance: ${total}"
        return result

    def __str__(self):
        return self.view_balance()