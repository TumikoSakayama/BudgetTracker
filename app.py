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
            'new_file': self.create_new_file:
            'load_file': self.load_existing_file,
            'save_file': self.save_file,
            'refresh': self.refresh_transaction_view
        }

        self.sidebar = Sidebar(self, sidebar_callbacks)
        self.sidebar_callbacks.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        self.form = TransactionForm(self.main_frame, self.add_transaction)
        self.from.grid(row=0, column=0, sticky='ew', padx=10, pady=(10, 5))

        self.display = TransactionDisplay(self.main_frame)
        self.display.grid(row=1, column=0, sticky='nsew', padx=10, pady=(5, 10))

    def create_new_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension = ".csv",
            filetypes = [("CSV files", ".csv"), ("All files", "*.*")]
        )

        if file_path:
            success, result = self.file_handler.create_new_file(file_path)

            if success:
                count, filename = result
                self.sidebar.update_file_label(label)
                self.form.enable_add_button()
                self.sidebar.enable_save()
                self.refresh_transaction_view()
                messagebox.showinfo("Success", "New Budget file created!")
            else:
                messagebox.showerror("Error", f"Failed to create file: {result}")

    