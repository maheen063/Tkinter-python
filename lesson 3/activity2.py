from tkinter import *
from tkinter import messagebox

# Create window
window = Tk()
window.title("Virus Scanner")
window.geometry("300x300")

def msg():
    #result = messagebox.askyesno("Delete.", "Are you sure?")
    messagebox.askyesno("Warning!", "Virus detected!")


button = Button(window, text="Scan for Virus.", command=msg)
button.place(x=40, y=80)

window.mainloop()