import customtkinter as ctk
from tkinter import filedialog, messagebox
from components import Sidebar, TransactionForm, TransactionDisplay
from fhandler import FileHandler

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class BudgetTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Budget Tracker")
        self.geometry("1000x700")

        self.file_handler = FileHandler()

        self.setup_layout()
        self.create_components()

    def setup_layout(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_components(self):
        sidebar_callbacks = {
            'new_file': self.create_new_file,
            'load_file': self.load_existing_file,
            'save_file': self.save_file,
            'refresh': self.refresh_transaction_view
        }

        self.sidebar = Sidebar(self, sidebar_callbacks)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        self.form = TransactionForm(self.main_frame, self.add_transaction)
        self.form.grid(row=0, column=0, sticky='ew', padx=10, pady=(10, 5))

        self.display = TransactionDisplay(self.main_frame)
        self.display.grid(row=1, column=0, sticky='nsew', padx=10, pady=(5, 10))

    def create_new_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension = ".csv",
            filetypes = [("CSV files", ".csv"), ("All files", "*.*")]
        )

        if file_path:
            success, result = self.file_handler.new_file(file_path)

            if success:
                self.sidebar.update_file_label(result)
                self.form.enable_add_button()
                self.sidebar.enable_save()
                self.refresh_transaction_view()
                messagebox.showinfo("Success", "New Budget file created!")
            else:
                messagebox.showerror("Error", f"Failed to create file: {result}")

    def load_existing_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".csv",
            filetypes = [("CSV files", ".csv"), ("All files", "*.*")]
        )

        if file_path:
            success, *result = self.file_handler.load_file(file_path)

            if success:
                count, filename = result
                self.sidebar.update_file_label(filename)
                self.form.enable_add_button()
                self.sidebar.enable_save()
                self.refresh_transaction_view()
                messagebox.showinfo("Success", f"Loaded {count} transactions!")
            else:
                messagebox.showerror("Error", f"Failed to load file: {result}")

    def add_transaction(self, data):
        if not self.file_handler.get_current_file():
            messagebox.showwarning("Warning", "Please create or load an existing file!")

        success, message = self.file_handler.add_transaction(
            data['Date'],
            data['Category'],
            data['Description'],
            data['Amount'],
            data['Type']
        )

        if success:
            self.form.clear_form()
            self.refresh_transaction_view()
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    def save_file(self):
        success, message = self.file_handler.save_file()

        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    def refresh_transaction_view(self):
        transactions = self.file_handler.get_transactions()
        self.display.update_transactions(transactions)

        total_income, total_expense, balance = self.file_handler.calculate_totals()
        self.display.update_summary(total_income, total_expense, balance)

        