from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Create window
root = Tk()
root.title("Event Handler")
root.geometry("300x300")

upload = Image.open("calculator.png")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(
    root,
    text="Hey! Welcome to the Denomination Calculator",
    bg='light blue'
)

def msg():
    topwin()

button1 = Button(
    root,
    text="Lets get started!!!",
    command=msg,
    bg='brown',
    fg='white'
)

button1.place(x=260, y=360)

def topwin():
    # top level widget
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("700x700")

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)

    lbl = Label(top,
                text="Here are number of notes for each denomination",
                bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            note2000, note500, note100, amount = 0, 0, 0, 0
            amount = int(entry.get())

            # no of notes needed
            # integer division
            note2000 = amount // 2000

            # modulus division
            amount %= 2000 # 1600

            if amount>0:
                note500 = amount // 500
                amount %= 500
                note100 = amount // 100

            # deletes previous entries
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            # insert values
            t1.insert(0, str(note2000))
            t2.insert(0, str(note500))
            t3.insert(0, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter valid amount")

    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")
    label.place(x=350, y=100)
    entry.place(x=250, y=130)
    btn.place(x=290, y=150)
    lbl.place(x=180, y=240)

    l1.place(x=350, y=250)
    l2.place(x=350, y=350)
    l3.place(x=350, y=450)

    t1.place(x=340, y=200)
    t2.place(x=340, y=230)
    t3.place(x=340, y=260)

root.mainloop()