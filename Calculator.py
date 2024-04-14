from tkinter import *
import math

root = Tk()
root.title('Simple Calculator')
input = Entry(root,width=25,borderwidth=5,font=('Arial',14))
input.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def click(number):
    current=input.get()
    input.delete(0, END)
    input.insert(0, str(current)+str(number))

def clear():
    input.delete(0,END)    

def add():
    first_number=input.get()
    global f_num 
    global op
    op='addition'
    f_num=int(first_number)
    input.delete(0,END)

def equals():
    second_number=input.get()
    input.delete(0,END)

    if op=='addition':
           input.insert(0, f_num + int(second_number)) 

    if op=='subtraction':
           input.insert(0, f_num - int(second_number)) 

    if op=='multiplication':
           input.insert(0, f_num * int(second_number)) 

    if op=='division':
           input.insert(0, f_num / int(second_number))  

    if op=='exponent':
           input.insert(0, f_num ** int(second_number))  

    if op=='square':
           input.insert(0, f_num ** 2)  

    if op=='squareroot':
           input.insert(0, math.sqrt(f_num))                       


def subtract():
    first_number=input.get()
    global f_num 
    global op 
    op='subtraction'
    f_num=int(first_number)
    input.delete(0,END)

def multiply():
    first_number=input.get()
    global f_num 
    global op 
    op='multiplication'
    f_num=int(first_number)
    input.delete(0,END)

def divide():
    first_number=input.get()
    global f_num 
    global op 
    op='division'
    f_num=int(first_number)
    input.delete(0,END)     

def exponent():
    first_number=input.get()
    global f_num 
    global op
    op='exponent'
    f_num=int(first_number)
    input.delete(0,END)

def square():
    first_number=input.get()
    global f_num 
    global op 
    op='square'
    f_num=int(first_number)
    input.delete(0,END)

def squareroot():
    first_number=input.get()
    global f_num 
    global op 
    op='squareroot'
    f_num=float(first_number)
    input.delete(0,END)   




myButton1 = Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='1',command=lambda: click(1))
myButton2 = Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='2',command=lambda: click(2))
myButton3 = Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='3',command=lambda: click(3))
myButton4 = Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='4',command=lambda: click(4))
myButton5 = Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='5',command=lambda: click(5))
myButton6 = Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='6',command=lambda: click(6))
myButton7 = Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='7',command=lambda: click(7))
myButton8 = Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='8',command=lambda: click(8))
myButton9 = Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='9',command=lambda: click(9))
myButton0 = Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='0',command=lambda: click(0))
myButtonplus= Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='+',command=add)
myButtonequals= Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='=',command=equals)
myButtonclear= Button(root,width=5,height=2,padx=45,pady=10,font=('Arial',12),text='Clear',command=clear)
myButtonsub= Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='-',command=subtract)
myButtonmul= Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='x',command=multiply)
myButtondiv= Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='/',command=divide)
myButtonexp= Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='^',command=exponent)
myButtonsqr= Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='x^2',command=square)
myButtonsqroot= Button(root,width=5,height=2,padx=10,pady=10,font=('Arial',12),text='sqrt(x)',command=squareroot)





myButton1.grid(row=1,column=0)
myButton2.grid(row=1,column=1)
myButton3.grid(row=1,column=2)
myButtonplus.grid(row=1,column=3)


myButton4.grid(row=2,column=0)
myButton5.grid(row=2,column=1)
myButton6.grid(row=2,column=2)
myButtonsub.grid(row=2,column=3)

myButton7.grid(row=3,column=0)
myButton8.grid(row=3,column=1)
myButton9.grid(row=3,column=2)
myButtonmul.grid(row=3,column=3)

myButton0.grid(row=4,column=0)
myButtonclear.grid(row=4,column=1,columnspan=2)
myButtondiv.grid(row=4,column=3)

myButtonexp.grid(row=5,column=0)
myButtonsqr.grid(row=5,column=1)
myButtonsqroot.grid(row=5,column=2)
myButtonequals.grid(row=5,column=3)







root.mainloop()