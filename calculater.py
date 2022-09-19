#Calculator 
from tkinter import *

win=Tk()
win.geometry('300x400')
win.resizable(height=True,width=True)

def f1():
    str1=en.get()
    ans1=eval(str1)
    en.delete(0,END)    
    en.insert(0,ans1)

def num(x):
    en.insert(END,x)

def operators(x):
    str1=en.get()
    if str1[-1] not in '+-*/.':
        str1=str1+x
        en.delete(0,END)    
        en.insert(0,str1)
    else:
        str1=str1[:-1]+x
        en.delete(0,END)
        en.insert(0,str1) 

def bk():
    str1=en.get()
    en.delete(0,END)
    en.insert(0,str1[:-1])   

frame=Frame(win,bg='black',width=400,height=300).pack(expand=True,fill=BOTH)

b1=Button(win,text='00',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:num('00')).place(x=10,y=350)
b1=Button(win,text='0',width=4,fg='blue',bg='yellow',font=('Arial',14,'bold'),command=lambda:num('0')).place(x=80,y=350)
b1=Button(win,text='.',width=4,fg='blue',bg='yellow',font=('Arial',14,'bold'),command=lambda:operators('.')).place(x=150,y=350)
b1=Button(win,text='=',width=4,fg='blue',bg='yellow',font=('Arial',14,'bold'),command=f1).place(x=220,y=350)

b1=Button(win,text='1',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:num('1')).place(x=10,y=300)
b1=Button(win,text='2',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:num('2')).place(x=80,y=300)
b1=Button(win,text='3',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:num('3')).place(x=150,y=300)
b1=Button(win,text='+',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:operators('+')).place(x=220,y=300)

b1=Button(win,text='4',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:num('4')).place(x=10,y=250)
b1=Button(win,text='5',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:num('5')).place(x=80,y=250)
b1=Button(win,text='6',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:num('6')).place(x=150,y=250)
b1=Button(win,text='-',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:operators('-')).place(x=220,y=250)

b1=Button(win,text='7',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:num('7')).place(x=10,y=200)
b1=Button(win,text='8',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:num('8')).place(x=80,y=200)
b1=Button(win,text='9',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:num('9')).place(x=150,y=200)
b1=Button(win,text='*',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:operators('*')).place(x=220,y=200)

b1=Button(win,text='CE',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:en.delete(0,END)).place(x=10,y=150)
b1=Button(win,text='C',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:en.delete(0,END)).place(x=80,y=150)
b1=Button(win,text='⌫',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=bk).place(x=150,y=150)
b1=Button(win,text='/',width=4,fg='blue',bg='yellow', font=('Arial',14,'bold'),command=lambda:operators('/')).place(x=220,y=150)

en=Entry(win,font=('Arial',14,'bold'),bg='white',fg='black',width=24,bd=2,justify=RIGHT)
en.place(x=10,y=100)

win.mainloop()