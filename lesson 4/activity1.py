from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

# Creating window
window = Tk()
window.title("Text Editor")
window.geometry("600x600")

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

current_file = None

# Function to open selected file
def open_file():
    global current_file

    # Open window to select file
    path = askopenfilename(filetypes=[("Text Files", "*.txt")], title="Open File")

    if not path:
        return
    
    try:
        with open (path, "r") as file:
            txt_edit.config(state="normal")
            txt_edit.insert(END, file.read())
    
    except:
        messagebox.showerror("Error", "Error occured while opening file.")

    current_file = path
    window.title(f"Text editor - {path}")

def save_file():
    if current_file is None:
        messagebox.showwarning("No File opened.")
        return
    
    try:
        with open(current_file, "w") as file:
            file.write(txt_edit.get("1.0", END))
        window.title("Text Editor - {current_file}")
    
    except:
        messagebox.showerror("Error!", "Could not save!")

def exit_app():
    answer = messagebox.askyesno("Exit", "Do you want to exit?")
    
    if answer:
        window.destroy()

# Widgets
btn_frame = Frame(window, bd=2, relief=RAISED)

btn_frame.grid(row=0, column=0, sticky="ns")

Button(btn_frame, text="Open", command=open_file).pack(padx=5, pady=10, fill="x")
Button(btn_frame, text="Save", command=save_file).pack(padx=5, pady=10, fill="x")
Button(btn_frame, text="Exit", command=exit_app).pack(padx=5, pady=10, fill="x")

# multi line text
txt_edit = Text(window, state="disabled")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()