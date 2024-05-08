from tkinter import *

window = Tk()
# window.geometry("400x400")
window.title("Program")
# =================== labels =============================
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)


l2 = Label(window, text="Author")
l2.grid(row=0, column=2)


l3 = Label(window, text="Year")
l3.grid(row=1, column=0)


l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# =================== Entries =============================
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

Author_text = StringVar()
e1 = Entry(window, textvariable=Author_text)
e1.grid(row=0, column=3)

Year_text = StringVar()
e1 = Entry(window, textvariable=Year_text)
e1.grid(row=1, column=1)

ISBN_text = StringVar()
e1 = Entry(window, textvariable=ISBN_text)
e1.grid(row=1, column=3)
# =================== Listbox =============================
lst = Listbox(window)
lst.grid(row=2, column=0, rowspan=6, columnspan=2)
lst.insert(END, "python")
sco = Scrollbar(window)
sco.grid(row=2, column=2, rowspan=6)
lst.configure(yscrollcommand=sco.set)
sco.configure(command=lst.yview)

# =================== Button =============================
b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)


window.mainloop()
