import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# ---------- Data Handling ----------
def load_data(filename, default_data):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump(default_data, f, indent=4)
    with open(filename, 'r') as f:
        return json.load(f)

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# ---------- Authentication ----------
def login():
    username = simpledialog.askstring("Login", "Enter username:")
    password = simpledialog.askstring("Login", "Enter password:", show='*')

    users = load_data('users.json', {"admin": "admin123"})

    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Login successful!")
        open_inventory_window()
    else:
        messagebox.showerror("Login", "Invalid username or password.")

def register():
    username = simpledialog.askstring("Register", "Enter new username:")
    if not username:
        return
    password = simpledialog.askstring("Register", "Enter new password:", show='*')
    if not password:
        return

    users = load_data('users.json', {"admin": "admin123"})

    if username in users:
        messagebox.showerror("Error", "Username already exists!")
    else:
        users[username] = password
        save_data('users.json', users)
        messagebox.showinfo("Success", f"User '{username}' registered successfully!")

# ---------- Inventory Functions ----------
def add_product():
    pid = simpledialog.askstring("Add Product", "Enter product ID:")
    name = simpledialog.askstring("Add Product", "Enter product name:")
    quantity = simpledialog.askinteger("Add Product", "Enter quantity:")
    price = simpledialog.askfloat("Add Product", "Enter price:")

    if not pid or not name or quantity is None or price is None:
        messagebox.showerror("Error", "All fields are required!")
        return

    if quantity < 0 or price < 0:
        messagebox.showerror("Error", "Quantity and price must be positive!")
        return

    inventory = load_data('data.json', {})
    inventory[pid] = {"name": name, "quantity": quantity, "price": price}
    save_data('data.json', inventory)

    messagebox.showinfo("Success", f"Product '{name}' added successfully!")

def edit_product():
    pid = simpledialog.askstring("Edit Product", "Enter product ID:")
    inventory = load_data('data.json', {})

    if pid not in inventory:
        messagebox.showerror("Error", "Product not found!")
        return

    name = simpledialog.askstring("Edit Product", "Enter new name:", initialvalue=inventory[pid]['name'])
    quantity = simpledialog.askinteger("Edit Product", "Enter new quantity:", initialvalue=inventory[pid]['quantity'])
    price = simpledialog.askfloat("Edit Product", "Enter new price:", initialvalue=inventory[pid]['price'])

    inventory[pid] = {"name": name, "quantity": quantity, "price": price}
    save_data('data.json', inventory)

    messagebox.showinfo("Success", f"Product '{pid}' updated successfully!")

def delete_product():
    pid = simpledialog.askstring("Delete Product", "Enter product ID:")
    inventory = load_data('data.json', {})

    if pid in inventory:
        del inventory[pid]
        save_data('data.json', inventory)
        messagebox.showinfo("Success", f"Product '{pid}' deleted successfully!")
    else:
        messagebox.showerror("Error", "Product not found!")

def view_low_stock():
    inventory = load_data('data.json', {})
    low_stock_items = [f"{pid} - {data['name']} (Qty: {data['quantity']})"
                       for pid, data in inventory.items() if data['quantity'] < 5]

    if low_stock_items:
        messagebox.showwarning("Low Stock", "\n".join(low_stock_items))
    else:
        messagebox.showinfo("Low Stock", "No low stock items.")

# ---------- GUI Windows ----------
def open_inventory_window():
    inv_window = tk.Toplevel(root)
    inv_window.title("Inventory Management")

    tk.Button(inv_window, text="Add Product", command=add_product).pack(pady=5)
    tk.Button(inv_window, text="Edit Product", command=edit_product).pack(pady=5)
    tk.Button(inv_window, text="Delete Product", command=delete_product).pack(pady=5)
    tk.Button(inv_window, text="Low Stock Report", command=view_low_stock).pack(pady=5)
    tk.Button(inv_window, text="Exit", command=inv_window.destroy).pack(pady=5)

# ---------- Main App ----------
root = tk.Tk()
root.title("Inventory System")
root.geometry("300x200")

tk.Button(root, text="Login", command=login).pack(pady=10)
tk.Button(root, text="Register", command=register).pack(pady=10)

root.mainloop()
