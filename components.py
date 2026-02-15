import customtkinter as ctk
from datetime import datetime

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, callbacks):
        super().__init__(master, width=200, corner_radius=0)
        self.callbacks = callbacks
        self.grid_rowconfigure(6, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.logo_label = ctk.CTkLabel(
            self,
            text="Budget Tracker",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.new_file_btn = ctk.CTkButton(
            self,
            text="New File",
            command=self.callbacks['new_file']
        )
        self.new_file_btn.grid(row=1, column=0, padx=20, pady=10)

        self.load_file_btn = ctk.CTkButton(
            self,
            text="Load Existing File",
            command=self.callbacks['load_file']
        )
        self.load_file_btn.grid(row=2, column=0, padx=20, pady=10)
        
        self.save_file_btn =ctk.CTkButton(
            self,
            text="Save File",
            command= self.callbacks['save_file'],
            state='disabled' 
        )
        self.save_file_btn.grid(row=3, column=0, padx=20, pady=10)

        self.refresh_btn = ctk.CTkButton(
            self,
            text="Refresh View",
            command=self.callbacks['refresh']
        )
        self.refresh_btn.grid(row=4, column=0, padx=20, pady=10)

        self.file_label = ctk.CTkLabel(
            self,
            text="No file loaded",
            wraplength=100,
            font=ctk.CTkFont(size=11)
        )
        self.file_label.grid(row=7, column=0, padx=20, pady=(0, 20))

    def enable_save(self):
        self.save_file_btn.configure(state='normal')

    def update_file_label(self, filename):
        self.file_label.configure(text=f"File: {filename}")

class TransactionForm(ctk.CTkFrame):
    def __init__(self, master, add_callback):
        super().__init__(master)
        self.add_callback = add_callback
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.form_title =ctk.CTkLabel(
            self,
            text="Add New Transaction",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.form_title.grid(row=0, column=0, columnspan=5, pady=10)

        ctk.CTkLabel(self, text="Date").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.date_entry = ctk.CTkEntry(self, placeholder_text='MM-DD-YYYY')
        self.date_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.date_entry.insert(0, datetime.now().strftime("%m-%d-%Y"))

        ctk.CTkLabel(self, text="Category").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.cat_entry = ctk.CTkEntry(self, placeholder_text="e.g. Food, Transport")
        self.cat_entry.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(self, text="Description").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.desc_entry = ctk.CTkEntry(self, placeholder_text="Transaction description")
        self.desc_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(self, text="Amount").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.amount_entry = ctk.CTkEntry(self, placeholder_text="0.00")
        self.amount_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(self, text="Type").grid(row=3, column=2, padx=5, pady=5, sticky="e")
        self.type_var = ctk.StringVar(value="Expense")
        self.type_menu = ctk.CTkOptionMenu(
            self,
            values=["Income", "Expense"],
            variable=self.type_var
        )
        self.type_menu.grid(row=3, column=3, padx=5, pady=5, sticky="ew")

        self.add_btn = ctk.CTkButton(
            self,
            text="Add Transaction",
            command=self.handle_add,
            state="disabled"
        )
        self.add_btn.grid(row=4, column=0, columnspan=5, padx=20, pady=15)

    def handle_add(self):
        data = self.get_form_data()
        self.add_callback(data)

    def get_form_data(self):
        return {
            'Date': self.date_entry.get().strip(),
            'Category': self.cat_entry.get().strip(),
            'Description': self.desc_entry.get().strip(),
            'Amount': self.amount_entry.get().strip(),
            'Type': self.type_var.get()
        }
    
    def clear_form(self):
        self.date_entry.delete(0, 'end')
        self.date_entry.insert(0, datetime.now().strftime("%m-%d-%Y"))
        self.cat_entry.delete(0, 'end')
        self.desc_entry.delete(0, 'end')
        self.amount_entry.delete(0, 'end')
    
    def enable_add_button(self):
        self.add_btn.configure(state="normal")

class TransactionDisplay(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.sort_column = None
        self.sort_reverse = False
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.summary_frame = ctk.CTkFrame(self)
        self.summary_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        self.summary_frame.grid_columnconfigure((0,1, 2), weight=1)

        self.total_income_label = ctk.CTkLabel(
            self.summary_frame,
            text="Total Income: $0.00",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="green"
        )
        self.total_income_label.grid(row=0, column=0, padx=10, pady=10)

        self.total_expense_label = ctk.CTkLabel(
            self.summary_frame,
            text="Total Expense: $0.00",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="red"
        )
        self.total_expense_label.grid(row=0, column=1, padx=10, pady=10)

        self.balance_label = ctk.CTkLabel(
            self.summary_frame,
            text="Balance: $0.00",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.balance_label.grid(row=0, column=2, padx=10, pady=10)

        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=(10, 0))

        self.header_frame.grid_columnconfigure((0, 1, 4), weight=1)
        self.header_frame.grid_columnconfigure(2, weight=2)
        self.header_frame.grid_columnconfigure(3, weight=1)
        self.header_frame.grid_columnconfigure(5, weight=0, minsize=100)

        self.date_btn = ctk.CTkButton(self.header_frame, text="Date", command=lambda: self.sort_by("Date"))
        self.date_btn.grid(row=0, column=0, sticky="ew", padx=5)

        self.cat_btn = ctk.CTkButton(self.header_frame, text="Category", command=lambda: self.sort_by("Category"))
        self.cat_btn.grid(row=0, column=1, sticky="ew", padx=5)

        self.desc_btn = ctk.CTkButton(self.header_frame, text="Description", command=lambda: self.sort_by("Description"))
        self.desc_btn.grid(row=0, column=2, sticky="ew", padx=5)

        self.amount_btn = ctk.CTkButton(self.header_frame, text="Amount", command=lambda: self.sort_by("Amount"))
        self.amount_btn.grid(row=0, column=3, sticky="ew", padx=(5, 30))

        self.type_btn = ctk.CTkButton(self.header_frame, text="Type", command=lambda: self.sort_by("Type"))
        self.type_btn.grid(row=0, column=4, sticky="ew", padx=5)

        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

    def update_transactions(self, transactions):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for i, transaction in enumerate(transactions, start=0):
            trans_frame = ctk.CTkFrame(
                self.scrollable_frame,
                fg_color="gray30" if i % 2 == 0 else "gray20"
            )
            trans_frame.grid(row=i, column=0, sticky="ew", padx=5, pady=2)

            trans_frame.grid_columnconfigure((0, 1, 4), weight=1)
            trans_frame.grid_columnconfigure(2, weight=2) 
            trans_frame.grid_columnconfigure(3, weight=1)
            trans_frame.grid_columnconfigure(5, weight=0, minsize=100)

            amount = float(transaction['Amount'])
            amount_color = "green" if transaction['Type'] == 'Income' else "red"

            ctk.CTkLabel(trans_frame, text=transaction['Date']).grid(row=0, column=0, padx=10, sticky="w")
            ctk.CTkLabel(trans_frame, text=transaction['Category']).grid(row=0, column=1, padx=10, sticky="w")
            ctk.CTkLabel(trans_frame, text=transaction['Description']).grid(row=0, column=2, padx=10, sticky="ew")
            ctk.CTkLabel(trans_frame, text=f"{amount:,.2f}", text_color=amount_color).grid(row=0, column=3, padx=(10, 40), sticky="e")
            ctk.CTkLabel(trans_frame, text=transaction['Type']).grid(row=0, column=4, padx=10, sticky="w")

            action_frame = ctk.CTkFrame(trans_frame, fg_color="transparent")
            action_frame.grid(row=0, column=5, sticky="nsew")

            edit_btn = ctk.CTkButton(
                action_frame, text="✏", width=30, height=28, fg_color="transparent",
                hover_color="gray35", command= lambda t=transaction: self.edit_transaction(t)
            )
            edit_btn.pack(side="left", padx=5)

            del_btn = ctk.CTkButton(
                action_frame, text="🗑", width=30, height=28, fg_color="transparent",
                hover_color="#8B0000", command= lambda t=transaction: self.delete_transaction(t)
            )
            del_btn.pack(side="left")

    def update_summary(self, total_income, total_expense, balance):
        self.total_income_label.configure(text=f"Total Income: ${total_income:,.2f}")
        self.total_expense_label.configure(text=f"Total Expense: ${total_expense:,.2f}")
        self.balance_label.configure(
            text=f"Total Balance: ${balance:,.2f}",
            text_color="green" if balance >=0 else "red"
        )

    def delete_transaction(self, transaction):
        file_handler = self.master.master.file_handler
        file_handler.transactions.remove(transaction)
        self.update_transactions(file_handler.get_transactions())
        total_income, total_expense, balance = file_handler.calculate_totals()
        self.update_summary(total_income, total_expense, balance)

    def edit_transaction(self, transaction):
        form = self.master.master.form
        form.date_entry.delete(0, "end")
        form.date_entry.insert(0, transaction["Date"])
        form.cat_entry.delete(0, "end")
        form.cat_entry.insert(0, transaction["Category"])
        form.desc_entry.delete(0, "end")
        form.desc_entry.insert(0, transaction["Description"])
        form.amount_entry.delete(0, "end")
        form.amount_entry.insert(0, transaction["Amount"])
        form.type_var.set(transaction["Type"])
        self.delete_transaction(transaction)

    def sort_by(self, column):
        self.sort_reverse = not self.sort_reverse
        self.date_btn.configure(text=f"Date {'↓' if self.sort_reverse else '↑'}" if column == "Date" else "Date")
        self.cat_btn.configure(text=f"Category {'↓' if self.sort_reverse else '↑'}" if column == "Category" else "Category")
        self.desc_btn.configure(text=f"Description {'↓' if self.sort_reverse else '↑'}" if column == "Description" else "Description")
        self.amount_btn.configure(text=f"Amount {'↓' if self.sort_reverse else '↑'}" if column == "Amount" else "Amount")
        self.type_btn.configure(text=f"Type {'↓' if self.sort_reverse else '↑'}" if column == "Type" else "Type")

        try:
            if column == "Amount":
                key_func = lambda x: float(x[column])
            else:
                key_func = lambda x: x[column].lower()
            
            self.master.master.file_handler.transactions.sort(key=key_func, reverse=self.sort_reverse)
        except: 
            pass
        
        self.update_transactions(self.master.master.file_handler.get_transactions())