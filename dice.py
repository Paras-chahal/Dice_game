from cProfile import label
import random
from tkinter import *

root=Tk()
root.geometry("600x300")

l1=Label(root,text='',font=("times",300))

def roll():
    number= ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

b1=Button(root,text="lets roll...",command=roll)

b1.place(x=250,y=0)

root.mainloop()