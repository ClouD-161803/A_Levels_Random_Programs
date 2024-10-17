import tkinter as tk                                                           #imports library

root= tk.Tk()                                                                  #creates a tk root widget

canvas1 = tk.Canvas(root, width = 400, height = 300)                           #creates canvas
canvas1.pack()                                                                 #puts widget in the frame

entry1 = tk.Entry (root)                                                       #assign input to a variable
canvas1.create_window(200, 140, window=entry1)                                 #creates window for the input

def getSquareRoot ():                                                          #defines subroutine
    label1=""                                                                  #creates blank label
    x1 = entry1.get()                                                          #assigns the input to x1 variable

    label1 = tk.Label(root, text= float(x1)**0.5)                              #calculates square root
    canvas1.create_window(200, 230, window=label1)                             #puts the result on thw window

button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)         #creates button
canvas1.create_window(200, 180, window=button1)                                #puts button on the window

root.mainloop()                                                                #loops the operation