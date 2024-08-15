import tkinter as tk
from tkinter import *
import pandas as pd


def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(en1.get())
            except Exception as e:
                value="Error"
        scvalue.set(value)
        en1.update()
    elif text == "C":
        scvalue.set("")
        en1.update()
    else:
        scvalue.set(scvalue.get() + text)
        en1.update()

cal = Tk()
cal.title("/*/ CALCULATOR /*/")
cal.minsize(height=600,width=400)
cal.maxsize(height=600,width=400)
cal.config(bg="gray")
cal.geometry()

lf=LabelFrame(cal,text="Digital",font=("Baskerville Old Face",15,"bold"),fg="white",height=575,width=375,labelanchor=N,background="black",borderwidth=4,relief="flat")
lf.place(x=10,y=10)

# photo=PhotoImage(file=r'C:\Users\kunal\OneDrive\Desktop\kunal\graphical1.py\modi.png')
# lab1=Label(lf,image=photo,height=75,width=210)
# lab1.place(x=75,y=460)



scvalue = StringVar()
scvalue.set(" ")
en1=Entry(lf,textvariable=scvalue,font=("Arial",25,"bold"),bg="light blue")
en1.place(x=10,y=5,width=350,height=80)




bt17=Button(lf,text="C",font=("Baskerville Old Face",10,"bold")
            ,height=1,width=5,relief="raised",borderwidth=3,bg="gray")
bt17.place(x=295,y=120)
bt17.bind("<Button-1>", click)

bt1=Button(lf,text="%",font=("Baskerville Old Face",20,"bold")
           ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt1.place(x=20,y=160)
bt1.bind("<Button-1>", click)

bt2=Button(lf,text="(",font=("Baskerville Old Face",20,"bold")
           ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt2.place(x=110,y=160)
bt2.bind("<Button-1>", click)

bt3=Button(lf,text=")",font=("Baskerville Old Face",20,"bold")
           ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt3.place(x=200,y=160)
bt3.bind("<Button-1>", click)

bt4=Button(lf,text="/",font=("Baskerville Old Face",20,"bold")
           ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt4.place(x=290,y=160)
bt4.bind("<Button-1>", click)

bt5=Button(lf,text="1",font=("Baskerville Old Face",20,"bold")
           ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt5.place(x=20,y=240)
bt5.bind("<Button-1>", click)

bt6=Button(lf,text="2",font=("Baskerville Old Face",20,"bold")
           ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt6.place(x=110,y=240)
bt6.bind("<Button-1>", click)

bt7=Button(lf,text="3",font=("Baskerville Old Face",20,"bold")
           ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt7.place(x=200,y=240)
bt7.bind("<Button-1>", click)

bt8=Button(lf,text="*",font=("Baskerville Old Face",20,"bold")
           ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt8.place(x=290,y=240)
bt8.bind("<Button-1>", click)

bt9=Button(lf,text="4",font=("Baskerville Old Face",20,"bold")
           ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt9.place(x=20,y=320)
bt9.bind("<Button-1>", click)

bt10=Button(lf,text="5",font=("Baskerville Old Face",20,"bold")
            ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt10.place(x=110,y=320)
bt10.bind("<Button-1>", click)

bt11=Button(lf,text="6",font=("Baskerville Old Face",20,"bold")
            ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt11.place(x=200,y=320)
bt11.bind("<Button-1>", click)

bt12=Button(lf,text="-",font=("Baskerville Old Face",20,"bold")
            ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt12.place(x=290,y=320)
bt12.bind("<Button-1>", click)

bt13=Button(lf,text="7",font=("Baskerville Old Face",20,"bold")
            ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt13.place(x=20,y=400)
bt13.bind("<Button-1>", click)

bt14=Button(lf,text="8",font=("Baskerville Old Face",20,"bold")
            ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt14.place(x=110,y=400)
bt14.bind("<Button-1>", click)

bt15=Button(lf,text="9",font=("Baskerville Old Face",20,"bold")
            ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt15.place(x=200,y=400)
bt15.bind("<Button-1>", click)

bt16=Button(lf,text="+",font=("Baskerville Old Face",20,"bold")
            ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt16.place(x=290,y=400)
bt16.bind("<Button-1>", click)

bt20=Button(lf,text=".",font=("Baskerville Old Face",20,"bold")
            ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt20.place(x=20,y=480)
bt20.bind("<Button-1>", click)

bt18=Button(lf,text="0",font=("Baskerville Old Face",20,"bold")
            ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt18.place(x=110,y=480)
bt18.bind("<Button-1>", click)

bt19=Button(lf,text="=",font=("Baskerville Old Face",20,"bold")
            ,height=1,width=3,relief="raised",borderwidth=3,bg="gray")
bt19.place(x=200,y=480,width=150)
bt19.bind("<Button-1>", click)

bt19.bind("<Return>", click)


# lf.bindtags(bt19,"<Return>", click)


cal.mainloop()



