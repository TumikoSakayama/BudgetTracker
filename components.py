import customtkinter as ctk
from datetime import datetime

class Sidebar(self):
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
        self.save_file_btn(state='normal')

    def update_file_label(self):
        self.file_label.configure(text=f"File: {filename}")

class TransactionForm:
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
        self.date_entry = ctk.CTkEntry(self, placeholder_text='MM-DD-YYYYY')
        self.date_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.date_entry.insert(0, datetime.now().strftime("%m-%d-%Y"))

        ctk.CTkLabel(self, text="Category").grid(row=1, column=, padx=5, pady=5, sticky="e")
        self.cat_entry = ctk.CTkEntry(self, placeholder_text="e.g. Food, Transport")
        self.cat_entry.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(self, text="Description").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.desc_entry = ctk.CTkEntry(self, placeholder_text="Transaction description")
        self.cat_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(self, text="Date").grid(row=1, column=0, padx=5, pady=5, sticky="e")
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
        return = {
            'date': self.date_entry.get().strip(),
            'category': self.cat_entry.get().strip(),
            'description': self.desc_entry.get().strip(),
            'amount': self.amount_entry.get().strip(),
            'type': self.type_var.get()
        }
    
    def clear_form(self):
        self.date_entry.delete(0, 'end')
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.category_entry.delete(0, 'end')
        self.description_entry.delete(0, 'end')
        self.amount_entry.delete(0, 'end')
    
    def enable_add_button(self):
        self.add_btn.configure(state="normal")

        
