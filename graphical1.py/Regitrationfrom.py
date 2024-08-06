import tkinter as tk
from tkinter import*
import sqlite3
import datetime
from tkinter import messagebox
# from tkcalendar import Calendar 

# def test():
#     print(var.get())

conn= sqlite3.connect(r"C:\Users\kunal\OneDrive\Desktop\kunal\graphical1.py\Regitrationfrom.db")
cur=conn.cursor()
# cur.execute(r"create table registration(Name varchar(20),Reg varchar(15),Address varchar(30),PassW varchar(20),DateofBairth varchar(15));")
# status=cur.fetchall()

root=Tk()
root.title(" Registrationnfrom ")
root.geometry()
root.minsize(height=600,width=400)
root.maxsize(height=600,width=400)
root.config(background="pink")



def test():
    if Name.get()== "" or cb == True:
        messagebox.showerror("Error","please All Fields are required!") 
    else:
        conn= sqlite3.connect(r"C:\Users\kunal\OneDrive\Desktop\kunal\graphical1.py\Regitrationfrom.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO registration VALUES(?,?,?,?,?)",(Name.get(),Reg.get(),Address.get(),PassW.get(),DateofBairth.get()))
        conn.commit()
        conn.execute("SELECT * FROM registration")
        conn.close()
        messagebox.showinfo("YES","sucessfully insserting in data ") 

Name=StringVar()
Reg=StringVar()
Address=StringVar()
PassW=StringVar()
DateofBairth=StringVar()

Frame1 = Frame(root,background="light blue",height=595,width=395,border=5,highlightbackground="black",highlightcolor="black",highlightthickness=3,relief="flat")
Frame1.place(x=3,y=3)

label2= Label(root,text="Loging page",font=("arial",10,"bold"),bg="light blue",relief="solid")
label2.place(x=170,y=10)

photo1 = PhotoImage(file='C:/Users/kunal/OneDrive/Desktop/kunal/graphical1.py/images.png')
label = Label(Frame1,image=photo1,height=90,width=90)
label.place(x=150,y=50)


var = IntVar()
height = 20
lab1 = Label(Frame1,text="Name :- ",font=("Sitka Heading Semibold",15,"bold"),bg="light blue")
lab1.place(x=25,y=height+150)

lab2 = Label(Frame1,text="Reg :- ",font=("Sitka Heading Semibold",15,"bold"),bg="light blue")
lab2.place(x=25,y=height+190)

lab3 = Label(Frame1,text="Address :- ",font=("Sitka Heading Semibold",15,"bold"),bg="light blue")
lab3.place(x=25,y=height+230)

lab4 = Label(Frame1,text="PassW :- ",font=("Sitka Heading Semibold",15,"bold"),bg="light blue")
lab4.place(x=25,y=height+270)

lab5 = Label(Frame1,text="Date of Birth :- ",font=("Sitka Heading Semibold",15,"bold"),bg="light blue")
lab5.place(x=25,y=height+310)






en1 = Entry(Frame1,width=20,font=("Arial",10,"bold"),textvariable=Name)
en1.place(x=160,y=height+160)

en1 = Entry(Frame1,width=20,font=("Arial",10,"bold"),textvariable=Reg)
en1.place(x=160,y=height+200)

en2 = Entry(Frame1,width=20,font=("Arial",10,"bold"),textvariable=Address)
en2.place(x=160,y=height+240)

en3 = Entry(Frame1,width=20,font=("Arial",10,"bold"),show="*",textvariable=PassW)
en3.place(x=160,y=height+280)

en4 = Entry(Frame1,width=20,font=("Arial",10,"bold"),textvariable=DateofBairth)
en4.place(x=160,y=height+320)

cb = Checkbutton(Frame1,text="Accepts the sure from filup",bg="light blue",font=("Arial",10,"underline","bold"),activebackground="light blue",variable=var,fg="black",activeforeground="white")
cb.place(x=77,y=height+420)

bt = Button(Frame1,text="Submit",font=("Arial",10,"bold"),relief="ridge",activebackground="white",activeforeground="black",command=test)
bt.place(x=130,y=height+450)
print(var.get())




root.mainloop()