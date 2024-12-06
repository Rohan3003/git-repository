import tkinter as tk
from tkinter import ttk, messagebox

# Main Application Class
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Hierarchy Navigation")
        self.root.geometry("400x300")

        # Start with the Login Page
        self.login_page()

    def login_page(self):
        """Login Page"""
        self.clear_frame()

        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.validate_login).pack(pady=10)

    def validate_login(self):
        """Validate Login and Navigate to BU Selection"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":  # Dummy check
            self.select_bu()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def select_bu(self):
        """Select Business Unit"""
        self.clear_frame()

        tk.Label(self.root, text="Select Business Unit", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="SBU 1", command=lambda: self.select_sbu("SBU 1")).pack(pady=5)
        tk.Button(self.root, text="SBU 2", command=lambda: self.select_sbu("SBU 2")).pack(pady=5)

    def select_sbu(self, bu):
        """Select Sub-Business Unit"""
        self.clear_frame()

        tk.Label(self.root, text=f"Selected {bu}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Select Sub-Business Unit").pack(pady=5)

        tk.Button(self.root, text="SBU 1", command=lambda: self.navigate_to_pages(bu, "SBU 1")).pack(pady=5)
        tk.Button(self.root, text="SBU 2", command=lambda: self.navigate_to_pages(bu, "SBU 2")).pack(pady=5)

    def navigate_to_pages(self, bu, sbu):
        """Navigate to Final Pages"""
        self.clear_frame()

        tk.Label(self.root, text=f"{bu} -> {sbu}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Select Page").pack(pady=5)

        tk.Button(self.root, text="BMO", command=lambda: self.show_page(bu, sbu, "BMO")).pack(pady=5)
        tk.Button(self.root, text="RBCCM", command=lambda: self.show_page(bu, sbu, "RBCCM")).pack(pady=5)
        tk.Button(self.root, text="RBCWM", command=lambda: self.show_page(bu, sbu, "RBCWM")).pack(pady=5)
        tk.Button(self.root, text="CS", command=lambda: self.show_page(bu, sbu, "CS")).pack(pady=5)
        tk.Button(self.root, text="MKTX", command=lambda: self.show_page(bu, sbu, "MKTX")).pack(pady=5)

    def show_page(self, bu, sbu, page):
        """Show Final Page"""
        self.clear_frame()

        tk.Label(self.root, text=f"{bu} -> {sbu} -> {page}", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text=f"Welcome to {page} Page!", font=("Arial", 12)).pack(pady=10)

        tk.Button(self.root, text="Back to BU Selection", command=self.select_bu).pack(pady=5)

    def clear_frame(self):
        """Clear all widgets from the frame"""
        for widget in self.root.winfo_children():
            widget.destroy()


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


