from tkinter import *
from tkinter import ttk

# =====================Setting====================

win = Tk()
win.geometry("300x200")
win.title("cal")
win.config(bg="gray")


# =====================Def====================

Numberlst=[]
def cal(number):
    if number.isdigit():
        Numberlst.append(number)
        resu.config(text =f'result: + {''.join(Numberlst)}')
    elif number == "=":
        try:
            result = eval("".join(Numberlst))
            resu.config(text="result: " + str(result))
        except:
            resu.config(text="result: Error")
    else:
        Numberlst.append(number)

# =====================Frame====================
part1 = Frame(win, width=300, height=90, bg="gray")
part1.pack(side=TOP)

part2 = Frame(win, width=300, height=90, bg="gray")
part2.pack(side=TOP)

part3 = Frame(win, width=300, height=90, bg="gray")
part3.pack(side=TOP)

part4 = Frame(win, width=300, height=90, bg="gray")
part4.pack(side=TOP)

part5 = Frame(win, width=300, height=90, bg="gray")
part5.pack(side=TOP)

part6 = Frame(win, width=300, height=90, bg="gray")
part6.pack(side=TOP)

# =====================Button====================
resu = Label(part1, text="result: ", width=39, height=2)
resu.pack()

btCE = ttk.Button(part2, text="CE", width=9, command=lambda: cal("CE"))
btCE.pack(side=LEFT, padx=2, pady=2)

C = ttk.Button(part2, text="C", width=9, command=lambda: cal("C"))
C.pack(side=LEFT, padx=2, pady=2)

delete = ttk.Button(part2, text="<--", width=9, command=lambda: cal("<--"))
delete.pack(side=LEFT, padx=2, pady=2)

div = ttk.Button(part2, text="/", width=9, command=lambda: cal("/"))
div.pack(side=LEFT, padx=2, pady=2)


Seven = ttk.Button(part3, text="7", width=9, command=lambda: cal('7'))
Seven.pack(side=LEFT, padx=2, pady=2)

Eight = ttk.Button(part3, text="8", width=9, command=lambda: cal('8'))
Eight.pack(side=LEFT, padx=2, pady=2)

Nine = ttk.Button(part3, text="9", width=9, command=lambda: cal('9'))
Nine.pack(side=LEFT, padx=2, pady=2)

mul = ttk.Button(part3, text="*", width=9, command=lambda: cal('*'))
mul.pack(side=LEFT, padx=2, pady=2)


Four = ttk.Button(part4, text="4", width=9, command=lambda: cal('4'))
Four.pack(side=LEFT, padx=2, pady=2)

Five = ttk.Button(part4, text="5", width=9, command=lambda: cal('5'))
Five.pack(side=LEFT, padx=2, pady=2)

Six = ttk.Button(part4, text="6", width=9, command=lambda: cal('6'))
Six.pack(side=LEFT, padx=2, pady=2)

minus = ttk.Button(part4, text="-", width=9, command=lambda: cal('-'))
minus.pack(side=LEFT, padx=2, pady=2)


one = ttk.Button(part5, text="1", width=9, command=lambda: cal('1'))
one.pack(side=LEFT, padx=2, pady=2)

tow = ttk.Button(part5, text="2", width=9, command=lambda: cal('2'))
tow.pack(side=LEFT, padx=2, pady=2)

tree = ttk.Button(part5, text="3", width=9, command=lambda: cal('3'))
tree.pack(side=LEFT, padx=2, pady=2)

plas = ttk.Button(part5, text="+", width=9, command=lambda: cal('+'))
plas.pack(side=LEFT, padx=2, pady=2)


pam = ttk.Button(part6, text="+/-", width=9, command=lambda: cal('+/-'))
pam.pack(side=LEFT, padx=2, pady=2)

ziro = ttk.Button(part6, text="0", width=9, command=lambda: cal('0'))
ziro.pack(side=LEFT, padx=2, pady=2)

flot = ttk.Button(part6, text=".", width=9, command=lambda: cal('.'))
flot.pack(side=LEFT, padx=2, pady=2)

result = ttk.Button(part6, text="=", width=9, command=lambda: cal('='))
result.pack(side=LEFT, padx=2, pady=2)


win.mainloop()