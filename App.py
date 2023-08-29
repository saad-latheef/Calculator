import tkinter as tk
win=tk.Tk()
win.title('Simple Calculator')
a=tk.Label(win, text='CALCULATOR (Only for whole numbers)', font=('Courier New',10) ).grid(row=0,column=0,columnspan=3)
e=tk.Entry(win, width=35, borderwidth=5)
e.grid(row=1,column=0, columnspan=3, padx=20, pady=10 )
def calc(l,count):
    nl=[]
    count1=0
    for i in l:
        if i.isdigit():
            nl.append(float(i))
        else:
            nl.append(i)
    print(nl)
    for i in range(count):
        for j in range(len(nl)):
            if nl[j]=='x':
                p=float(nl[j-1])
                q=float(nl[j+1])
                nl[j-1]=p*q
                del nl[j]
                del nl[j]
                break
            if nl[j]=='÷':
                p=float(nl[j-1])
                q=float(nl[j+1])
                nl[j-1]=p/q
                del nl[j]
                del nl[j]
                break
            if nl[j]=='+' or nl[j]=='-':
                count1+=1
    for i in range(count1):
        for j in range(len(nl)):
            if nl[j]=='+':
                p=float(nl[j-1])
                q=float(nl[j+1])
                nl[j-1]=p+q
                del nl[j]
                del nl[j]
                break
            if nl[j]=='-':
                p=float(nl[j-1])
                q=float(nl[j+1])
                nl[j-1]=p-q
                del nl[j]
                del nl[j]
                break    
    print(nl)
    e.delete(0, tk.END)
    e.insert(0,nl[0])
def add(n):
    po=e.get()
    e.delete(0, tk.END)
    e.insert(0,po+str(n))
def take():
    count=0
    h=''
    qtn=e.get()
    if str(qtn[0]).isdigit():
        for i in qtn:
            if i.isdigit() or i=='.':
                ddasdsds=0
            else:
                h=h+' '+i+' '
                count=count+1
                continue
            h=h+i
        l=h.split()
        calc(l,count)
    else:
        e.delete(0, tk.END)
        e.insert(0,'Syntax Error')
def clr():
    e.delete(0,tk.END)
b1=tk.Button(win,text=1,padx=40,pady=20,command=lambda: add(1))
b2=tk.Button(win,text=2,padx=40,pady=20,command=lambda: add(2))
b3=tk.Button(win,text=3,padx=40,pady=20,command=lambda: add(3))
b4=tk.Button(win,text=4,padx=40,pady=20,command=lambda: add(4))
b5=tk.Button(win,text=5,padx=40,pady=20,command=lambda: add(5))
b6=tk.Button(win,text=6,padx=40,pady=20,command=lambda: add(6))
b7=tk.Button(win,text=7,padx=40,pady=20,command=lambda: add(7))
b8=tk.Button(win,text=8,padx=40,pady=20,command=lambda: add(8))
b9=tk.Button(win,text=9,padx=40,pady=20,command=lambda: add(9))
b0=tk.Button(win,text=0,padx=90,pady=20,command=lambda: add(0))
bp=tk.Button(win,text='+',font=('Ariel'),padx=40,pady=20,command=lambda: add('+'))
bm=tk.Button(win,text='-',font=('Ariel'),padx=40,pady=20,command=lambda: add('-'))
bmu=tk.Button(win,text='x',font=('Ariel'),padx=40,pady=20,command=lambda: add('x'))
bd=tk.Button(win,text='÷',font=('Ariel'),padx=40,pady=20,command=lambda: add('÷'))
be=tk.Button(win,text='=',font=('Ariel'),padx=88,pady=20,command=take)
bc=tk.Button(win,text='AC',font=('Ariel'),padx=32,pady=20,command=clr)

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)

b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)

b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)

b0.grid(row=5,column=0,columnspan=2)
bp.grid(row=5,column=2)
bm.grid(row=6,column=0)
bd.grid(row=6,column=1)
bmu.grid(row=6,column=2)

be.grid(row=7,column=0,columnspan=2)
bc.grid(row=7,column=2)

win.mainloop()