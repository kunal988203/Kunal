import tkinter as tk
from tkinter import*
from tkinter import ttk

changed=0

# def function1():
#     lab3.config(text="love you") # type: ignore


# def function2():
#     global changed
#     if changed == 0:
#         config(text="3. This my work place ")
#         lab3.config(text=" kunal")
#         changed=1
#     else:
#         lable3.config(text="")
#         lab3.config(text="Hii")
#         changed=0

# def test():
#     print(var.get())


# # def fun():
# #     Lab1.config(text=" file not found  ")

win =Tk()
win.title(" PYTHON ")  # windows title cange command
# win.maxsize(height=666,width=500)
# win.minsize(height=666,width=500)
win.geometry("500x500")


# var = BooleanVar()

# photo2=PhotoImage(file=r'C:\Users\kunal\OneDrive\Desktop\kunal\graphical1.py\apple.png')
# win.iconphoto(True,photo2)   # windos logo change command

# #win.attributes("-alpha",0.5)  # windos blur command

# win.config()   # windos background colour change

# # photo1=PhotoImage(file=r'C:/Users/kunal/OneDrive/Desktop/kunal/graphical1.py/image12.png')
# # lab4=Label(win,image=photo1)
# # lab4.place(x=0,y=0,)




# '''systemwidth = win.winfo_screenwidth()
# systemheight = win.winfo_screenheight()

# centerx = int(systemwidth/2 - width/2)
# centery = int(systemheight/2 - height/2)

# win.geometry(f"{systemheight}x{width}+{centerx}+{centery}")''' # windos size increse and decrese command

# def new_func3(win):
#     lab3=Label(win, text="HIII", font=("Goudy Stout",15),fg="white",
#             bg="black",cursor="tcross",relief="sunken",justify="right")
#     lab3.place(x=160,y=110)



#     lab1=Label(win, text="hello python " , font=("Algerian",20,"bold"),
#            fg="white",bg="black",cursor="man")                           
#     lab1.place(x=80,y=10)              #lable box window set command  


#     lab2=Label(win, text="WORLS", font=("Harlow Solid Italic",20),
#            fg="white",bg="black",cursor="man",underline=6)
#     lab2.place(x=200,y=67)

# new_func3(win)


# # variable = StringVar(win,value="python",name="s")
# # variable = IntVar(win,value=9878383767003)
# # variable = BooleanVar(win,value=True,name="b")
# # variable = DoubleVar(win,value=23.65,name="d")
# # print(variable.get())


# labframe1=LabelFrame(win,text="python",font=("Harlow Solid Italic",30,"bold"),fg="red",labelanchor=N,border=10,borderwidth=10,relief="flat")
# labframe1.place(x=300,y=200,height=300,width=1000)
# # labframe1.pack(padx=400,pady=400)


# def new_func2(labframe1):
#     lable1=Label(labframe1,text="1. This is your pen.",font=("Harlow Solid Italic",25))
#     lable1.place(x=0,y=0)

#     lable2=Label(labframe1,text="2. This is your book.",font=("Harlow Solid Italic",20))
#     lable2.place(x=0,y=45)

#     lable3=Label(labframe1,text="",font=("Harlow Solid Italic",20))
#     lable3.place(x=0,y=90)

# new_func2(labframe1)



# bt = Button(win,text="Submit",font=20,fg="red",command=function1)
# bt.place(x=40,y=150)
# bt2 = Button(labframe1,text="On",font=("Baskerville Old Face",10,"bold"),fg="blue",relief="raised",bg="yellow",command=function2)
# bt2.place(x=250,y=100,height=20,width=60)



# ##{  checkbutton using function 
# def new_func1(test, win, var, labframe1):
#     cb=Checkbutton(labframe1,text="School",height=2,width=10,activeforeground="blue",font=("Harlow Solid Italic",15,"bold"),bd=4,variable=var)
#     cb.place(x=100,y=150)
#     buttan = Button(win,text="school",font=(25),command=test)
#     buttan.pack()
#     print(var.get())
# new_func1(test, win, var, labframe1)
# ## }

# #radiobutton
# def new_func(labframe1):
#     rd=Radiobutton(labframe1,text="love",value="python",relief="raised",)
#     rd.place(x=500,y=70)
#     rd.deselect()
#     rd1=Radiobutton(labframe1,text="don't love",value="java",relief="raised",highlightbackground="blue",)
#     rd1.place(x=500,y=100,height=23,width=100)
#     rd1.deselect()

# new_func(labframe1)

# #menu button 
# # menuB = Menubutton(win,text="File")
# # menuB.menu = Menu(menuB,tearoff=0)
# # menuB["menu"]=menuB.menu
# # menuB.menu.add_checkbutton(label="New file",command=fun)
# # menuB.menu.add_checkbutton(label="Open file")
# # menuB.menu.add_checkbutton(label="Save file")
# # menuB.place(x=600,y=550)



# def new():
#     print("File is not found")

# #menu buttom
# file_menu = Menu(win)
# f_menu = Menu(file_menu,tearoff=0)
# f_menu.add_command(label="New file",command=new)

# #sub_menu
# sub_menu = Menu(f_menu,tearoff=0)
# sub_menu.add_command(label="kunal.py")
# sub_menu.add_command(label="mou.py")
# sub_menu.add_command(label="Gour.py")
# sub_menu.add_command(label="Gopal.py")
# sub_menu.add_command(label="krishna.py")
# sub_menu.add_command(label="shuva.py")
# f_menu.add_cascade(label="Open file",menu=sub_menu)


# f_menu.add_command(label="Save file")
# f_menu.add_separator()
# f_menu.add_command(label="Save as file")
# win.config(menu=file_menu)
# file_menu.add_cascade(label='File',menu=f_menu)

# file_menu1 = Menu(win)
# f_menu1 = Menu(file_menu1,tearoff=0)
# f_menu1.add_command(label="Cut")
# f_menu1.add_command(label="Copy")
# f_menu1.add_separator()
# f_menu1.add_command(label="Paste")
# f_menu1.add_command(label="Undo")
# file_menu.add_cascade(label='Edit',menu=f_menu1)



# def value_change(var):
#     var = value.get()
#     lb.config(text=var)

# #opthion menu
# oplist = ["AI","Python","Java","Tk"]
# value =StringVar()
# value.set("Subject")
# op = OptionMenu(win,value,*oplist,command=value_change)
# op.place(x=100,y=250,height=30)
# lb = Label(win,text=" ",background="pink")
# lb.place(x=100,y=300,height=40)




# Entry box
# def mail():
#     labble.config(text=ks.get())
 
# ks = StringVar()

# en = Entry(win,cursor="Plus",justify="center",bd=3,show="*",textvariable=ks)
# en.place(x=180,y=350)

# but = Button(win,text="click",command=mail)
# but.place(x=180,y=375)

# labble =Label(win,text=" ",font=("bold"),bd=8,background="pink",justify="center")
# labble.place(x=180,y=400,width=150,height=27)




#Text box 
# def pyto():
#     var=text.get("1.0","end")
#     labble1.config(text=var)

# text = Text(win,height=10,width=50,bg="light yellow")
# text.place(x=10,y=440)
# but1 = Button(win,text="click1",command=pyto)
# but1.place(x=10,y=600)
# labble1 = Label(win,text="",bg="pink")
# labble1.place(x=170,y=650,height=250,width=500)




#combo box
def combox():
    c = comb10.get()
    label10.config(text=c)
list_1 = ["react","django","pandas","plegon"]
comb10=StringVar()
combo10 = ttk.Combobox(win,values=list_1,font=(10),textvariable=comb10)
combo10.set("subject ")
combo10.place(x=600,y=560)

# buton10 = Button(win,text="ok",font=(8),command=combox)
# buton10.place(x=600,y=600) 

# label10 = Label(win,text="",font=(10))
# label10.place(x=600,y=650)


# #notebook widgt

# notebook = ttk.Notebook(win)
# notebook.pack(pady=100,expand=True)

# frame1 =ttk.Frame(notebook)
# frame1.pack(fill="both",expand=True)

# lableframe1 = Label(frame1,text="python")
# lableframe1.place(x=900,y=300)

# frame2 =ttk.Frame(notebook)
# frame2.pack(fill="both",expand=True)

# lableframe2 = Label(frame1,text="python")
# lableframe2.place(x=900,y=400)

# notebook.add(frame1,text="New")
# notebook.add(frame2,text="Open")


win.mainloop()