# Unit Converter Tool

from tkinter import *
import tkinter.messagebox as box

root = Tk()
root.title('Unit Converter Tool')

# Dropdown Units Widget
options = ['Miles to Km', 'Km to Miles']
clicked = StringVar()
clicked.set('Select Conversion')
drop = OptionMenu(root, clicked, *options).grid()

# Enter Value Widget
entry = Entry(root, width=30, borderwidth=10).grid() 

# Functions
def miles():
    x = float(entry.get())
    y = x / 1.609
    miles = str(y)
    label = Label(root,text=miles + ' Miles').grid()
    return label
        
def km():
    x = float(entry.get())
    y = x * 1.609
    kms = str(y)
    label2 = Label(root, text=kms + ' Kms').grid()
    return labe2

def calc1(): 
    if clicked.get() == 'Miles to Km':
        return km()
        
    if clicked.get() == 'Km to Miles':
        return miles()
    
button = Button(root, text='calculate', command=calc1).grid()

root.mainloop()