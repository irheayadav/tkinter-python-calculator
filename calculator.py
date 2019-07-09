##CALCULATOR In python

import tkinter as tk
from tkinter import messagebox

mainwindow = tk.Tk()
mainwindow.title("calculator")

heading_label_1 = tk.Label(mainwindow, text="Enter first value")
heading_label_1.pack()
name_field1 = tk.Entry(mainwindow)
name_field1.pack()

heading_label_2 = tk.Label(mainwindow, text="Enter second value")
heading_label_2.pack()
name_field2 = tk.Entry(mainwindow)
name_field2.pack()

heading_label_3 = tk.Label(mainwindow, text="operators")
heading_label_3.pack()


def addition():
    var1 = int(name_field1.get())
    var2 = int(name_field2.get())
    result = var1 + var2
    # print(sum)
    result_label.config(text="operation result is "+ str(result))

add = tk.Button(mainwindow, text="+", command=lambda: addition())
add.pack()


def substraction():
    var1 = int(name_field1.get())
    var2 = int(name_field2.get())
    if var1 < var2:
        messagebox.showerror("error", "first number has smaller value then second number")
    else:
        result = var1 - var2
        # print(diff)
    result_label.config(text="operation result is " + str('result'))

subtract = tk.Button(mainwindow, text="-", command=lambda: substraction())
subtract.pack()


def multiplication():
    var1 = int(name_field1.get())
    var2 = int(name_field2.get())
    result = var1 * var2
    # print(mul)
    result_label.config(text="operation result is "+ str(result))

multiply = tk.Button(mainwindow, text="*", command=lambda: multiplication())
multiply.pack()



def division():
    var1 = float(name_field1.get())
    var2 = float(name_field2.get())
    if var2 == 0:
        messagebox.showerror("error", "number could not be divide by zero")
    else:
        result = var1 / var2
        # print(div)
    result_label.config(text="operation result is " + str('result'))

divide = tk.Button(mainwindow, text="/", command=lambda: division())
divide.pack()


result_label = tk.Label(mainwindow, text="operation result is :")
result_label.pack()


mainwindow.mainloop()