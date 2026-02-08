import csv
import os
from tkinter import messagebox

class FileHandler:
    def __init__(self):
        self.current_file = None
        self.transactions = []

    def new_file(self, file_path):
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date','Category','Description','Amount','Type'])

                self.current_file = file_path
                self.transactions = []
                return True, os.path.basename(file_path)
        except Exception as e:
            return False, str(e)

    def load_file(self, file_path):
        try:
            self.transactions = []
            with open(file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.transactions.append(reader)
            
            self.current_file = file_path
            return True, len(self.transactions), os.path.basename(file_path)
        except Exception as e:
            raise False, str(e)


    def save_file(self, file_path):
        if not self.current_file:
            return False, "No File to Save!"

        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames= ['Date', 'Category', 'Description', 'Amount', 'Type']
                )
                writer.writeheader()
                writer.writerows(self.transactions)
            return True ,"File save successfully"
        except Exception as e:
            raise False, str(e)

    def add_transaction(self, date, category_name, description, amount, t_ype):
        if not all([date, category_name, description, amount]):
            return False, "Please fill in all the details!"

        try:
            float(amount)
        except ValueError:
            raise False, "Amount must be a number"

        transaction = {
            'Date':date,
            'Category':category_name,
            'Description':description,
            'Amount',amount,
            'Type':t_type
        }

        self.transactions.append(transaction)
        return True, "Transaction added successfully"

    def get_transactions(self):
        return self.transactions

    def calculate_totals(self):
        total_income = 0
        total_expense = 0

        for transaction in transactions:
            amount = float(transaction['Amount'])
            if transaction['Type'] == 'Income' :
                total_income += amount
            else:
                total_expense += amount

        balance = total_income - total_expense
        return total_income, total_expense

    def get_current_file(self):
        return self.current_file

    def get_file_name(self):
        if self.current_file:
            return os.path.basename(self.current_file)
        return "No file loaded!"            