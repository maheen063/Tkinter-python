from tkinter import *

# Create window
window = Tk()
window.title("Event Handler")
window.geometry("300x300")

def handle_keypress(event):
    print("Some key has been pressed")
    print(event.keysym)

# Binding the event and handler
window.bind("<BackSpace>", handle_keypress)

def handle_click(event):
    print("\n The button was pressed!")

button = Button(text="Don't click me!")
button.pack()

# Bind button click event and handler as well
button.bind("<ButtonRelease>", handle_click)

window.mainloop()