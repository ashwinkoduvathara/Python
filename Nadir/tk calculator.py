from tkinter import *
def addNumbers():
    sum=int(e1.get())+int(e2.get())
    result.set(sum)
def subtractNumbers():
    sub=int(e1.get())-int(e2.get())
    result.set(sub)
def multiNumbers():
    product=int(e1.get())*int(e2.get())
    result.set(product)
def divNumbers():
    divide=int(e1.get())/int(e2.get())
    result.set(divide)
calculator=Tk()
result=StringVar()
calculator.title('Calculator')
Label(calculator,text='Enter the 1st number: ',font='25').grid(row=0)
Label(calculator,text='Enter the 2nd number: ',font='25').grid(row=1)
Label(calculator,text='Result: ',font='25').grid(row=2)
res=Label(calculator,text='',textvariable=result).grid(row=2,column=1)
e1=Entry(calculator)
e2=Entry(calculator)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
btn1=Button(calculator,text='Add',font='10',command=addNumbers)
btn1.grid(row=0,column=2)
btn2=Button(calculator,text='Subtract',font='10',command=subtractNumbers)
btn2.grid(row=0,column=3)
btn3=Button(calculator,text='Product',font='10',command=multiNumbers)
btn3.grid(row=1,column=2)
btn4=Button(calculator,text='Division',font='10',command=divNumbers)
btn4.grid(row=1,column=3)
mainloop()