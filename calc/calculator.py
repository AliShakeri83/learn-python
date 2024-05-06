from tkinter import *
import tkinter.messagebox

# ============================== Setting ==============================
root = Tk()

root.geometry("300x200")

root.title("calculator")

root.resizable(width=False, height=False)

root.config(bg="gray")
# ============================== Variables ==============================
num1 = StringVar()
num2 = StringVar()
result_value = StringVar()
# ============================== Part ==============================
part1 = Frame(root, width=300, height=100, bg="gray")
part1.pack(side=TOP)

part2 = Frame(root, width=300, height=100, bg="gray")
part2.pack(side=TOP)

part3 = Frame(root, width=300, height=100, bg="gray")
part3.pack(side=TOP)

part4 = Frame(root, width=300, height=100, bg="gray")
part4.pack(side=TOP)


# ============================== functions ==============================
def errorMsg(msg1):
    if msg1 == "error":
        tkinter.messagebox.showerror("error", "wrong")
    elif msg1 == "ZeroDivisionError":
        tkinter.messagebox.showerror("error", "divided by zero")


def plus():
    result = float(num1.get()) + float(num2.get())
    result_value.set(result)


def minus():
    result = float(num1.get()) - float(num2.get())
    result_value.set(result)


def mul():
    result = float(num1.get()) * float(num2.get())
    result_value.set(result)


def div():
    if num2.get() == 0:
        errorMsg("division zero error")
    try:
        result = float(num1.get()) / float(num2.get())
        result_value.set(result)
    except:
        errorMsg("ZeroDivisionError")


# ============================== Buttons ==============================
bt_plus = Button(part3, text="+", width=9, command=plus)
bt_plus.pack(side=LEFT, padx=2)

bt_minus = Button(part3, text="-", width=9, command=minus)
bt_minus.pack(side=LEFT, padx=2)

bt_mul = Button(part3, text="*", width=9, command=mul)
bt_mul.pack(side=LEFT, padx=2)

bt_div = Button(part3, text="/", width=9, command=div)
bt_div.pack(side=LEFT, padx=2)

# ============================== Entries and Labels ==============================
lb1 = Label(part1, text="Enter your number 1: ")
lb1.pack(side=LEFT, padx=3, pady=3)
bt1 = Entry(part1, text="", textvariable=num1)
bt1.pack(side=LEFT, padx=10, pady=10)


lb2 = Label(part2, text="Enter your number 2: ")
lb2.pack(side=LEFT, padx=3, pady=3)
bt2 = Entry(part2, text="", textvariable=num2)
bt2.pack(side=LEFT, padx=10, pady=10)


lb3 = Label(part4, text="result: ")
lb3.pack(side=LEFT, padx=3, pady=3)
bt3 = Entry(part4, text="", textvariable=result_value)
bt3.pack(side=LEFT, padx=10, pady=10)

root.mainloop()
