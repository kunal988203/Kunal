import sqlite3 
from tkinter import *
from pandas import DataFrame
from tkinter import messagebox
from tkinter.messagebox import Message


conn = sqlite3.connect(r"C:\Users\kunal\OneDrive\Desktop\kunal\graphical1.py\test.db")
cur=conn.cursor()
# cur.execute(r"create table patient(date int(2) , month int(2),year int(5));")
# status=cur.fetchall()

def submit():
    data=en1.get()
    if data != "" or data.isspace==False:
        isdot=(lambda data : True if data.index(".") != -1 else False )(data)
        isslash=(lambda data : True if data.index("/") != -1 else False )(data)
        if isdot == True and isslash ==True:
            messagebox.showerror("wrong input")
        elif isdot == False and isslash ==False:
            messagebox.showerror("wrong input")
        elif isdot == True:
            dataARRAY=data.split(".")
        elif isslash == True:
            dataARRAY=data.split("/")
        if len(dataARRAY) != 3:
            messagebox.showerror("wrong input")
        else:
            day=int(dataARRAY[0])
            month=int(dataARRAY[1])
            year=int(dataARRAY[2])
            if day > 31 or month >12:
                messagebox.showerror("wrong input")
            else:
                cur.execute(f'''insert into patient values({day},{month},{year});''')
                conn.commit()
    else:
        messagebox.showerror("empty input","enter value")

    en1.delete(0,END)
    cur.execute(f'''insert into patient values ();''')
    conn.commit()
def get_val():
    cur.execute("select * from patient;")
    data=cur.fetchall()
    data = DataFrame(data)
    print(data)


root=Tk()
en1=Entry(root,)
en1.pack()

b1=Button(root,text="submit" , command=submit)
b1.pack()
b2=Button(root,text="get",command=get_val)
b2.pack()



root.mainloop()
conn.close()