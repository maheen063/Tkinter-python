import tkinter as tk
from datetime import date

# Creating the window
root = tk.Tk()
root.title("Simple App")
root.geometry("500x500")

# Creates label
tk.Label(root, text="Full Name", bg="#3895D3").pack(fill="x")

tk.Label(root, text="Enter your name:").pack()

# Input field to enter our name
name_entry = tk.Entry(root)
name_entry.pack()

output_box = tk.Text(root, height=4)
output_box.pack()

def display():
    name = name_entry.get()
    output_box.delete("1.0", tk.END) # Clear previous text

    output_box.insert(tk.END, f"Hello {name}! \n")
    output_box.insert(tk.END, "Welcome to the application :) \n")
    output_box.insert(tk.END, f"Todays date id {date.today()}")

    name_entry.delete(0, tk.END)

tk.Button(root, text="Begin!", command=display).pack()

root.mainloop()