from tkinter import *

window = Tk()


def action(var):
    e1.insert(END, var)


def equals():
    a = eval(e1_value.get())
    e1.delete(0, END)
    e1.insert(END, a)
    print(a)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, width=25)
e1.grid(row=0, column=0, rowspan=1, columnspan=4)

b1 = Button(window, text="1", width=4, command=lambda: action(1))
b1.grid(row=3, column=0)

b2 = Button(window, text="2", width=4, command=lambda: action(2))
b2.grid(row=3, column=1)

b3 = Button(window, text="3", width=4, command=lambda: action(3))
b3.grid(row=3, column=2)

b4 = Button(window, text="4", width=4, command=lambda: action(4))
b4.grid(row=4, column=0)

b5 = Button(window, text="5", width=4, command=lambda: action(5))
b5.grid(row=4, column=1)

b6 = Button(window, text="6", width=4, command=lambda: action(6))
b6.grid(row=4, column=2)

b7 = Button(window, text="7", width=4, command=lambda: action(7))
b7.grid(row=5, column=0)

b8 = Button(window, text="8", width=4, command=lambda: action(8))
b8.grid(row=5, column=1)

b9 = Button(window, text="9", width=4, command=lambda: action(9))
b9.grid(row=5, column=2)

b10 = Button(window, text="/", width=4, command=lambda: action('/'))
b10.grid(row=6, column=3)

b11 = Button(window, text="+", width=4,  command=lambda: action('+'))
b11.grid(row=3, column=3)

b12 = Button(window, text="-", width=4, command=lambda: action('-'))
b12.grid(row=4, column=3)

b13 = Button(window, text="*", width=4, command=lambda: action('*'))
b13.grid(row=5, column=3)

b13 = Button(window, text="0", width=4, command=lambda: action(0))
b13.grid(row=6, column=1)

b14 = Button(window, text="=", width=4, command=equals)
b14.grid(row=2, column=3)

b15 = Button(window, text=".", width=4, command=lambda: action('.'))
b15.grid(row=6, column=0)

b16 = Button(window, text="%", width=4, command=lambda: action('%'))
b16.grid(row=6, column=2)

b17 = Button(window, text="Clear", width=15)
b17.grid(row=1, column=0, rowspan=2, columnspan=3)






window.mainloop()