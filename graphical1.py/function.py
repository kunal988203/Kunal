# #user definaed function is used def and lambda
# def kunal(f,t):
#     if f<t:
#         print(t)
#     else:
#         print(f)
# kunal(45,66)




# # sum=lambda a,b:(a+b)
# # h=sum(4,5)
# # print(h)



# def mul(*a):
#     s=0
#     for i in a:
#         s+=i
#     print(s)
# mul(3,10)








from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo,showerror, showwarning
from tkinter.messagebox import askretrycancel

# def kuna():
#     a=e1.get()
#     l1.config(text=a,)

kunal=Tk()
# # kunal.geometry("900x900")
# kunal.title(" kunal ")
# kunal.config(bg="light blue")
# kunal.maxsize(600,600)
# kunal.minsize(600,600)

# vivo=Label(kunal,text=" KUNAL SHIT ",fg="Black",bg="blue",font=("Algerian",25,"underline","bold"))
# vivo.pack(padx=200,pady=10)

# vivo1=Label(kunal,text="Adult",fg="yellow",bg="pink",font=("Algerian",12))
# vivo1.place(y=200,x=60)

# butten1=Button(kunal,text="submit",fg="red",bg="black",
#                activebackground="pink",activeforeground="blue",
#                 font=("Algerian",8),width=7,height=1,
#                 relief="flat")
# butten1.place(x=440,y=20)

# e1=Entry(kunal,)
# e1.pack(padx=200,pady=70)
# l1=Label(kunal,width=10)
# l1.pack(padx=200,pady=105)

# butten2=Button(kunal,text="submit",fg="black",bg="white",width=8,height=1,command=kuna)
# butten2.pack(padx=300,pady=100)


#separator line()
# lab1 =Label(kunal,text="kunal",background="blue")
# lab1.pack()

# separator = ttk.Separator(kunal,orient="vertical")
# separator.pack(fill=X)

# lab2=Label(kunal,text="shit")
# lab2.pack()

# #spin box()
# def py():
#     lab3.config(text=str(ks.get()))

# ks = IntVar()
# spinbox = Spinbox(kunal,from_=10, to=20,wrap=True,textvariable=ks,command=py)
# spinbox.pack()

# lab3 = Label(kunal,text="",bg="white",height=2,width=20)
# lab3.pack()



#scale box 
def sca(p):
    p = str(var.get())
    lab4.config(text=p)
var = DoubleVar()
scale = Scale(kunal,from_=0,to=100,orient="horizontal",activebackground="white",bg="light blue",variable=var,command=sca)
scale.place(x=10,y=100,width=200,height=50)

lab4 = Label(kunal,text="",font=("bold",20),height=2,width=10)
lab4.place(x=10,y=160)



# text = Text(kunal,font=("Baskerville Old Face",10,"bold"),bg="pink",fg="red")
# text.place(x=0,y=0,height=600,width=600)

# scrollbar = Scrollbar(text,orient="vertical",command=text.yview,cursor="arrow")
# scrollbar.place(x=580,y=0,height=590,width=20)

# scrollbar = Scrollbar(text,orient="horizontal",command=text.yview,cursor="arrow")
# scrollbar.place(x=0,y=580,height=20,width=580)

# text["yscrollcommand"]=scrollbar.set



#notebook widgt

# notebook = ttk.Notebook(kunal)
# notebook.pack(pady=100,expand=True)

# frame1 =ttk.Frame(notebook,height=500,width=500)
# frame1.pack(fill="both",expand=True)

# lableframe1 = Label(frame1,text="python")
# lableframe1.place(x=900,y=300)

# frame2 =ttk.Frame(notebook)
# frame2.pack(fill="both",expand=True)

# lableframe2 = Label(frame2,text="java",fg="black")
# lableframe2.place(x=900,y=400)

# notebook.add(frame1,text="New")
# notebook.add(frame2,text="Open")

# scrolledText  = ScrolledText(kunal,font=("bold",10),bg="light blue",fg="black")
# scrolledText.place(x=10,y=20,height=400,width=250)


#massagebox 
# def massbox():
#     showwarning(message="This is wrong password ")

# button = Button(kunal,text="OK",command=massbox)
# button.place(x=30,y=20)

#statusbar

# def change():
#     global change
#     if change == 0:
#         status_bar.config(text="READY to RACE")
#         change=1
#     else:
#         status_bar.config(text="OK")
#         change = 0

# status_bar = Label(kunal,text=" ",font=(5),relief="flat",bg="grey",cursor="heart")
# status_bar.pack(side=BOTTOM,fill=X)
# button1 = Button(status_bar,text="OK",bg="grey",activebackground="grey",command=change)
# button1.place(x=30,y=0)


#retrycancel 

# def retry():
#     answer = askretrycancel(title="wrong",message="This is a wrong password")

#     if answer:
#           retry()
#           if password == 988203 :
#                 lab2.get(text="procesed")
# ks = IntVar()
# password = Entry(kunal,width=20,font=("Arial",10,"bold"),show="*",textvariable=ks)
# password.place(x=150,y=120)

# lab2 = Label(kunal,text=" ")
# lab2.place(x=250,y=150)

# bt2 = Button(kunal,text="submit",command=retry)
# bt2.place(x=150,y=150)

# def mail():
#     labble.config(text=ks.get())

# en = Entry(win,cursor="Plus",justify="center",bd=3,show="*",textvariable=ks)
# en.place(x=180,y=350)

kunal.mainloop()