from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Tables")

title = Label(window,text="Mathematical Tables")
caption = Label(window,text="Number and Range")
title.grid(row=0,column=0,columnspan=3,padx=50,pady=15)
caption.grid(row=1,column=0,padx=10)

num = IntVar()
numbers = Combobox(window,textvariable=num,width=10)

numbers["values"] = tuple(range(101))

option = IntVar()
r10 = Radiobutton(window,variable=option,text="10",value=10)
r20 = Radiobutton(window,variable=option,text="20",value=20)
r30 = Radiobutton(window,variable=option,text="30",value=30)
option.set(10)

numbers.grid(row=2,column=0,pady=5)
r10.grid(row=2,column=2)
r20.grid(row=3,column=2,pady=5)
r30.grid(row=4,column=2,pady=5)

def GenMulTables():
    tables = ""
    for i in range(option.get()+1):
        tables += str(num.get()) + "  X  "  + str(i) + "  =  " + str(num.get()*i) + "\n"

    table.config(text=tables)

gen_btn = Button(window,text="Generate",command=GenMulTables)
table = Label(window,anchor=CENTER)

gen_btn.grid(row=4,column=0)
table.grid(row=5,column=0,columnspan=3,pady=25)

window.mainloop()