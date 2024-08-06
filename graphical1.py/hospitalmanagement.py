from tkinter import*
import tkinter as tk
from tkinter import ttk
from turtle import heading
import sqlite3
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
import datetime
from tkinter import messagebox

#---------------------------------data based conected in sqlite3--------------------------------

conn= sqlite3.connect(r"C:\Users\kunal\OneDrive\Desktop\kunal\graphical1.py\hospitalmanagement.db")
cur=conn.cursor()
# cur.execute(r"create table patients(NameofMedicien varchar(30),R_code varchar(10),Dose varchar(3),Dailydose varchar(3),lot varchar(5),Issuedate text(20),ExpaireDate text(20),Effect varchar(30),NHS varchar(20),P_Name varchar(20),DOB text(20),Address varchar(30),Gender varchar(10),PhoneNo int(12),Bloodpreasure int(5));")
# status=cur.fetchall()


#-------------------------------------------------------------stating for main windows --------------------------
root=Tk()
root.title("🚑 Hospital management🦽")
root.geometry("1540x800+0+0")
root.config(background="light blue")

icon = PhotoImage(file="c:\\Users\\kunal\\OneDrive\\Pictures\\zoom_in-64.png")
root.iconphoto(False,icon)

#-------------------------------------------------------------------functionality----------------------

# def openfile():
#     img = filedialog.askopenfile()
    




def iPrescription():
    if NameofMedicien.get()== "" or R_code.get()=="":
        messagebox.showerror("Error","please All Fields are required!")
    else:
        conn= sqlite3.connect(r"C:\Users\kunal\OneDrive\Desktop\kunal\graphical1.py\hospitalmanagement.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO patients VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(NameofMedicien.get(),
                                                                                R_code.get(),
                                                                                Dose.get(),
                                                                                Dailydose.get(),
                                                                                lot.get(),
                                                                                Issuedate.get(),
                                                                                ExpaireDate.get(),
                                                                                Effect.get(),
                                                                                NHS.get(),
                                                                                P_Name.get(),
                                                                                DOB.get(),
                                                                                Address.get(),
                                                                                Gender.get(),
                                                                                Phone_No.get(),
                                                                                Bloodpreasure.get(),
                                                                                Ocupetion.get(),
                                                                                DoctorName.get(),
                                                                                Information.get()
                                                                                ))
        conn.commit()
        conn.execute("SELECT * FROM patients")
        fatch()
        conn.close()
        messagebox.showinfo("yes","insert into record sucessfully")
                                                              


def fatch():
    conn= sqlite3.connect(r"C:\Users\kunal\OneDrive\Desktop\kunal\graphical1.py\hospitalmanagement.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM patients")
    rows=cur.fetchall()
    if len(rows)!=0:
        table.delete(*table.get_children())
        for i in rows:
            table.insert("",END,values=i)
        conn.commit()
        conn.close()

def cursor(event=" "):
    row=table.focus()
    content=table.item(row)
    row2=content["values"]
    NameofMedicien.set(row2[0])
    R_code.set(row2[1])
    Dose.set(row2[2])
    Dailydose.set(row2[3])
    lot.set(row2[4])
    Issuedate.set(row2[5])
    ExpaireDate.set(row2[6])
    Effect.set(row2[7])
    NHS.set(row2[8])
    P_Name.set(row2[9])
    DOB.set(row2[10])
    Address.set(row2[11])
    Gender.set(row2[12])
    Phone_No.set(row2[13])
    Bloodpreasure.set(row2[14])
    Ocupetion.set(row2[15])
    DoctorName.set(row2[16])
    Information.set(row2[17])
    conn.close()

def iupdate():
    conn= sqlite3.connect(r"C:\Users\kunal\OneDrive\Desktop\kunal\graphical1.py\hospitalmanagement.db")
    cur=conn.cursor()
    cur.execute("UPDATE patients SET NameofMedicien=?,Dose=?,Dailydose=?,lot=?,Issuedate=?,ExpaireDate=?,Effect=?,NHS=?,P_Name=?,DOB=?,Address=?,Gender=?,PhoneNo=?,Bloodpreasure=?,Ocupetion=?,DoctorName=?,Information=? WHERE R_code=?",(
                                                                                                                                                                                                                                            NameofMedicien.get(),
                                                                                                                                                                                                                                            Dose.get(),
                                                                                                                                                                                                                                            Dailydose.get(),
                                                                                                                                                                                                                                            lot.get(),
                                                                                                                                                                                                                                            Issuedate.get(),
                                                                                                                                                                                                                                            ExpaireDate.get(),
                                                                                                                                                                                                                                            Effect.get(),
                                                                                                                                                                                                                                            NHS.get(),
                                                                                                                                                                                                                                            P_Name.get(),
                                                                                                                                                                                                                                            DOB.get(),
                                                                                                                                                                                                                                            Address.get(),
                                                                                                                                                                                                                                            Gender.get(),
                                                                                                                                                                                                                                            Phone_No.get(),
                                                                                                                                                                                                                                            Bloodpreasure.get(),
                                                                                                                                                                                                                                            Ocupetion.get(),
                                                                                                                                                                                                                                            DoctorName.get(),
                                                                                                                                                                                                                                            Information.get(),
                                                                                                                                                                                                                                            R_code.get()
                                                                                                                                                                                                                                            ))  
    conn.commit()
    fatch()
    conn.close()
    messagebox.showinfo("Update_data","update sucessfully")                                                                                                                                                                                                                               



NameofMedicien=StringVar()
R_code=StringVar()
Dose=StringVar()
Dailydose=StringVar()
lot=StringVar()
Issuedate=StringVar()
ExpaireDate=StringVar()
Effect=StringVar()
NHS=StringVar()
P_Name=StringVar()
DOB=StringVar()
Address=StringVar()
Gender=StringVar()
Phone_No=StringVar()
Bloodpreasure=StringVar()
Ocupetion=StringVar()
DoctorName=StringVar()
Information=StringVar()


#==================================================photo image and icon ===========================
photo1 = PhotoImage(file="C:/Users/kunal/OneDrive/Pictures/blue-heart-pulse-monitor-signal-260nw-1375675052.png")
Label1 = Label(root,image=photo1,height=130)
Label1.place(x=0,y=35)
photo2 = PhotoImage(file="C:/Users/kunal/OneDrive/Pictures/blue-heart-pulse-monitor-signal-260nw-1375675052.png")
Label2 = Label(root,image=photo2,height=130,bg="#22608E")
Label2.place(x=390,y=35)
photo3 = PhotoImage(file="C:/Users/kunal/OneDrive/Pictures/blue-heart-pulse-monitor-signal-260nw-1375675052.png")
Label3 = Label(root,image=photo3,height=130,bg="#22608E")
Label3.place(x=780,y=35)
photo4 = PhotoImage(file="C:/Users/kunal/OneDrive/Pictures/blue-heart-pulse-monitor-signal-260nw-1375675052.png")
Label4 = Label(root,image=photo4,height=130,bg="#22608E")
Label4.place(x=1170,y=35)


#-------------------------------------------------------------------- Institute Name ------------------------------------------
Label1 = Label(root,font=("Engravers MT",15,"bold"),text=("➕ krismou Nursing-Home ➕"),fg="white",bd=5,relief="ridge",background="black",height=0,width=59)
Label1.pack(side=TOP,fill="x")

#--------------------------------------------------------------------frame is patient information ------------------------- 
Dataframe1 =Frame(root,bd=5,relief="ridge",bg="black")
Dataframe1.place(x=0,y=160,height=400,width=1530)

LabelFrame1 =LabelFrame(Dataframe1,text=("Patients Details"),font=("Arials",15,"bold"),labelanchor="n",bd=5,relief="groove",height=380,width=965)
LabelFrame1.place(x=3,y=5)

LabelFrame2 =LabelFrame(Dataframe1,text="Prescription",font=("Arials",15,"bold"),bd=5,relief="groove",height=380,width=540,labelanchor="n")
LabelFrame2.place(x=975,y=5)

detailsFrame3 = Frame(root,bd=5,relief="sunken",bg="black")
detailsFrame3.place(x=2,y=550,height=230,width=1525)

#-------------all Lable----------------------------------------------------------patient details ------------------


Label2 = Label(LabelFrame1,text="Medicien",font=("arials",10,"bold"),bg="black")
Label2.place(x=10,y=5)

Label3 = Label(LabelFrame1,text="Reference code",font=("arials",10,"bold"))
Label3.place(x=10,y=40)

Label4 = Label(LabelFrame1,text="Dose",font=("arials",10,"bold"))
Label4.place(x=10,y=75)

Label5 = Label(LabelFrame1,text="Daily Dose ",font=("arials",10,"bold"))
Label5.place(x=10,y=110)

Label6 = Label(LabelFrame1,text="Lot",font=("arials",10,"bold"))
Label6.place(x=10,y=145)

Label7 = Label(LabelFrame1,text="Issue Date",font=("arials",10,"bold"))
Label7.place(x=10,y=180) 

Label8 = Label(LabelFrame1,text="Expire Date",font=("arials",10,"bold"))
Label8.place(x=10,y=215)

Label9 = Label(LabelFrame1,text="Side-Effect",font=("arials",10,"bold"))
Label9.place(x=10,y=250)

Label10 = Label(LabelFrame1,text="NHS Number",font=("arials",10,"bold"))
Label10.place(x=10,y=285)

Label11 = Label(LabelFrame1,text="P-Name",font=("arials",10,"bold"))
Label11.place(x=560,y=5)

Label12 = Label(LabelFrame1,text="Date of birth",font=("arials",10,"bold"))
Label12.place(x=560,y=40)

Label13 = Label(LabelFrame1,text="Address",font=("arials",10,"bold"))
Label13.place(x=560,y=75)

Label14 = Label(LabelFrame1,text="Sex",font=("arials",10,"bold"))
Label14.place(x=560,y=110)

Label15 = Label(LabelFrame1,text="Phone_No.",font=("arials",10,"bold"))
Label15.place(x=560,y=145)

Label16 = Label(LabelFrame1,text="Blood Prasure",font=("arials",10,"bold"))
Label16.place(x=560,y=180)

Label17 = Label(LabelFrame1,text="Ocupetion",font=("arials",10,"bold"))
Label17.place(x=560,y=215)

Label18= Label(LabelFrame1,text="Doctor Name",font=("arials",10,"bold"))
Label18.place(x=560,y=250)

Label18= Label(LabelFrame1,text="Others Information",font=("arials",10,"bold"))
Label18.place(x=560,y=285)


# Label20=Label2 = Label(LabelFrame1,text="Photo",font=("arials",10,"bold"))
# Label20.place(x=450,y=10)
# Buttonfile = Button(LabelFrame1, text="Choose File",command=lambda:openfile())
# Buttonfile.place(x=440, y=40)
 

#-------------all Entry----------------------------------------------------------patient details ------------------


combobox1 = ttk.Combobox(LabelFrame1, font=("arials",10,"bold"),width=30,height=10,textvariable=NameofMedicien)
combobox1["values"] = ("Peracetamol", "Metrogel", "Covid-19","Combiflam","Vitamin D",
                       "Aspirin","Tylenol","Ibuprofen","Panadol","Omega-3",
                       "Vitamin B12","Vitamin B6","Vitamin B1","Vit","B2",
                       "Vitamin B3","Vitamin B5","Vitamin B","Evion 400","Cetzine")
combobox1.place(x=160,y=5)

combobox2 = ttk.Combobox(LabelFrame1,font=("arials",10,"bold"),width=30,height=10,textvariable=Gender)
combobox2["values"] = ("Male","Female","Trasngender","Others")
combobox2.place(x=690, y=110)

entry1 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=R_code)
entry1.place(x=160,y=40)

entry2 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=Dose)
entry2.place(x=160,y=75)

entry3 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33, textvariable=Dailydose)
entry3.place(x=160,y=110)

entry4 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=lot)
entry4.place(x=160,y=145)

entry5 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=Issuedate)
entry5.place(x=160,y=180)

entry6 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=ExpaireDate)
entry6.place(x=160,y=215)

entry7 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=Effect)
entry7.place(x=160,y=250)

entry8 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=NHS)
entry8.place(x=160,y=285)

entry9 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=P_Name)
entry9.place(x=690,y=5)

entry10 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=DOB)
entry10.place(x=690, y=40)

entry11 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=Address)
entry11.place(x=690, y=75)

entry14 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=Phone_No)
entry14.place(x=690, y=145)

entry15 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=Bloodpreasure)
entry15.place(x=690, y=180)

entry16 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=Ocupetion)
entry16.place(x=690, y=215)

entry17 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=DoctorName)
entry17.place(x=690, y=250)

entry18 = Entry(LabelFrame1, font=("arials",10,"bold"), width=33,textvariable=Information)
entry18.place(x=690, y=285)







#-------------------------------data frame showing-----------------------prascription-------------------------------------------

root.txtprescription =Text(LabelFrame2,font=("arials",10,"bold"),height=21,width=74,bd=2,bg="#fdfbe0")
root.txtprescription.place(x=0,y=0)

#-------------all button----------------------------------------------------------patient details ------------------

Button1 = Button(LabelFrame1, text="Save", font=("arials",10,"bold"), bg="light green")
Button1.place(x=572, y=320)

Button2 = Button(LabelFrame1, text="Update", font=("arials",10,"bold"), bg="yellow",command=iupdate)
Button2.place(x=743, y=320)

Button3 = Button(LabelFrame1, text="Delete", font=("arials",10,"bold"), bg="orange")
Button3.place(x=803, y=320)

Button4 = Button(LabelFrame1, text="Clear", font=("arials",10,"bold"), bg="red")
Button4.place(x=858, y=320)

Button5 = Button(LabelFrame1, text="Exit", font=("arials",10,"bold"), bg="Black",fg="white")
Button5.place(x=905, y=320)

Button6 = Button(LabelFrame1, text="Print Prescription", font=("arials",10,"bold"), bg="light blue",command=iPrescription)
Button6.place(x=618, y=320)


#-------------------------table create-----------------------------------------------------------
#----------------------scroll bar---------------------------data showing-------------------------

Scrollbarx = Scrollbar(detailsFrame3, orient=HORIZONTAL,repeatdelay=1000, jump=True,repeatinterval=10)
Scrollbary = Scrollbar(detailsFrame3, orient=VERTICAL, repeatdelay=100)

table=ttk.Treeview(detailsFrame3,columns=("NameofMedicien",
                                               "R_code",
                                               "Dose",
                                               "Dailydose",
                                               "lot",
                                               "Issuedate",
                                               "ExpaireDate",
                                               "Effect",
                                               "NHS",
                                               "P_Name",
                                               "DOB",
                                               "Address",
                                               "Gender",
                                               "Phone_No",
                                               "Bloodprasure",
                                               "Ocupetion",
                                               "DoctorName",
                                               "Information"),xscrollcommand=Scrollbarx.set
                                                        ,yscrollcommand=Scrollbary.set)

Scrollbarx.pack(side=BOTTOM,fill=X)
Scrollbary.pack(side=RIGHT,fill=Y,)

Scrollbarx=ttk.Scrollbar(command=table.xview)
Scrollbary=ttk.Scrollbar(command=table.yview)

table.heading("NameofMedicien",text="Name of Medicien")
table.heading("R_code",text="R_code")
table.heading("Dose",text="Dose")
table.heading("Dailydose",text="Daily dose")
table.heading("lot",text="Lot")
table.heading("Issuedate",text="Issue date")
table.heading("ExpaireDate",text="Expaire Date")
table.heading("Effect",text="Effect")
table.heading("NHS",text="NHS")
table.heading("P_Name",text="Name")
table.heading("DOB",text="DOB")
table.heading("Address",text="Address")
table.heading("Gender",text="Gender")
table.heading("Phone_No",text="Phone_No")
table.heading("Bloodprasure",text="Blood preasure")
table.heading("Ocupetion",text="Ocupetion")
table.heading("DoctorName",text="Name of Doctor")
table.heading("Information",text="Information")
table["show"]="headings"
table.pack(fill=BOTH,expand=1)
fatch()

table.column("NameofMedicien",width=105)
table.column("R_code",width=60)
table.column("Dose",width=50)
table.column("Dailydose",width=70)
table.column("lot",width=50)
table.column("Issuedate",width=80)
table.column("ExpaireDate",width=80)
table.column("Effect",width=80)
table.column("NHS",width=80)
table.column("P_Name",width=100)
table.column("DOB",width=80)
table.column("Address",width=100)
table.column("Gender",width=70)
table.column("Phone_No",width=100)
table.column("Bloodprasure",width=50)
table.column("Ocupetion",width=100)
table.column("DoctorName",width=100)
table.column("Information",width=100)

table.bind("<ButtonRelease-1>",cursor)










root.mainloop()





