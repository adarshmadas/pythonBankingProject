import tkinter as tk
from tkinter import messagebox

# Simulated "database" for storing user data
accounts = {}

# Function to create an account
def create_account():
    username = entry_username.get()
    password = entry_password.get()
    if username in accounts:
        messagebox.showerror("Error", "Account already exists!")
    else:
        accounts[username] = {'password': password, 'balance': 0.0}
        messagebox.showinfo("Success", "Account created successfully!")

# Function to login
def login():
    username = entry_username.get()
    password = entry_password.get()
    if username in accounts and accounts[username]['password'] == password:
        messagebox.showinfo("Login Success", "Welcome, " + username)
        show_main_menu(username)
    else:
        messagebox.showerror("Error", "Invalid credentials!")

# Function to show main menu after login
def show_main_menu(username):
    # Hide login screen
    login_frame.pack_forget()
    
    # Create main menu screen
    main_menu_frame.pack()
    
    label_balance.config(text="Balance: $" + str(accounts[username]['balance']))
    
    # Deposit button
    def deposit():
        amount = float(entry_deposit.get())
        if amount > 0:
            accounts[username]['balance'] += amount
            label_balance.config(text="Balance: $" + str(accounts[username]['balance']))
            messagebox.showinfo("Deposit", f"${amount} deposited!")
        else:
            messagebox.showerror("Error", "Enter a valid amount.")

    # Withdraw button
    def withdraw():
        amount = float(entry_withdraw.get())
        if amount > 0 and amount <= accounts[username]['balance']:
            accounts[username]['balance'] -= amount
            label_balance.config(text="Balance: $" + str(accounts[username]['balance']))
            messagebox.showinfo("Withdraw", f"${amount} withdrawn!")
        else:
            messagebox.showerror("Error", "Insufficient balance or invalid amount.")

    # Create deposit & withdraw functionalities
    label_deposit = tk.Label(main_menu_frame, text="Deposit Amount:")
    label_deposit.pack()
    entry_deposit = tk.Entry(main_menu_frame)
    entry_deposit.pack()
    deposit_button = tk.Button(main_menu_frame, text="Deposit", command=deposit)
    deposit_button.pack()

    label_withdraw = tk.Label(main_menu_frame, text="Withdraw Amount:")
    label_withdraw.pack()
    entry_withdraw = tk.Entry(main_menu_frame)
    entry_withdraw.pack()
    withdraw_button = tk.Button(main_menu_frame, text="Withdraw", command=withdraw)
    withdraw_button.pack()

# Setup window
root = tk.Tk()
root.title("Online Banking System")
root.geometry("300x400")

# Login Screen
login_frame = tk.Frame(root)

label_username = tk.Label(login_frame, text="Username:")
label_username.pack()
entry_username = tk.Entry(login_frame)
entry_username.pack()

label_password = tk.Label(login_frame, text="Password:")
label_password.pack()
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack()

create_account_button = tk.Button(login_frame, text="Create Account", command=create_account)
create_account_button.pack()

login_frame.pack()

# Main Menu Screen
main_menu_frame = tk.Frame(root)

label_balance = tk.Label(main_menu_frame, text="Balance: $0.0")
label_balance.pack()

# Start the GUI loop
root.mainloop()
