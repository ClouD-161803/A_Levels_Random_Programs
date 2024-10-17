import math

import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 600)
canvas1.pack()

entry1 = tk.Entry (root)
canvas1.create_window(200, 100, window=entry1)

entry2 = tk.Entry (root)
canvas1.create_window(200, 200, window=entry2)

entry3 = tk.Entry (root)
canvas1.create_window(200, 300, window=entry3)

label10 = tk.Label(root, text="Enter total amount")
canvas1.create_window(200, 80, window=label10)

label11 = tk.Label(root, text="Enter number of months")
canvas1.create_window(200, 180, window=label11)

label12 = tk.Label(root, text="Enter interest percentage")
canvas1.create_window(200, 280, window=label12)

def mortCalc ():
    tot = float(entry1.get())
    leng = float(entry2.get())
    ints = float(entry3.get())

    month_amount = tot/leng
    multiplier = 1+ints
    interest = month_amount*multiplier

    label1 = tk.Label(root, text=interest)
    canvas1.create_window(200, 500, window=label1)

button1 = tk.Button(text='Get Monthly mortgage', command=mortCalc)
canvas1.create_window(200, 400, window=button1)

root.mainloop()