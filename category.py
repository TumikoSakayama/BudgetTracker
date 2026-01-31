from transaction import Transaction

class Category:
    def __init__(self, name):
        self.name = name
        self.income_transactions = []
        self.expense_transactions = []

    def add_transaction(self, amount, name, transaction_type):
        if transaction_type == 'income':
            self.income_transactions.append(Transaction(amount, name))
        elif transaction_type == 'expense':
            self.expense_transactions.append(Transaction(amount, name))
        else:
            print("Invalid transaction type. Please enter 'income' or 'expense'.")

    def calculate_balance(self):
        total_income = sum(transaction.amount for transaction in self.income_transactions)
        total_expense = sum(transaction.amount for transaction in self.expense_transactions)
        return total_income - total_expense