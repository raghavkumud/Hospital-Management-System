# Booking Appointments
import mysql.connector
import tkinter
from tkinter import *
myw = Tk()
myw.configure(bg='#341adb')
myw.geometry('1518x1000')
myw.state('zoomed')

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="proca213")
mycursor = mydb.cursor()
# mycursor.execute("Create Database mydatabase")
# mycursor.execute("Create table appointment(id int Auto_Increment Primary Key,fname VARCHAR(50),lname VARCHAR(50),phone int,age int, gender varchar(20),doctor varchar(50))")

a = ""
b = ""
c = ""
d = ""
e = ""
f = ""

lb1 = Label(myw, text="Book Appointment", bg='#e3614f')
lb1.place(x=350, y=20)
lb1.config(font=('Garamond', 40, 'bold'))

lb2 = Label(myw, text="First Name", bg='#605691')
lb2.place(x=60, y=200)
lb2.config(font=('Garamond', 18))
e2 = Entry(myw, bg='#d68f42')
e2.place(x=400, y=200)
e2.config(font=('Garamond', 18))

lb6 = Label(myw, text="Last Name", bg='#605691')
lb6.place(x=850, y=200)
lb6.config(font=('Garamond', 18))
e6 = Entry(myw, bg='#d68f42')
e6.place(x=1050, y=200)
e6.config(font=('Garamond', 18))

lb3 = Label(myw, text="Phone Number", bg='#605691')
lb3.place(x=60, y=300)
lb3.config(font=('Garamond', 18))
e3 = Entry(myw, bg='#d68f42')
e3.place(x=400, y=300)
e3.config(font=('Garamond', 18))

lb4 = Label(myw, text="Age", bg='#605691')
lb4.place(x=850, y=300)
lb4.config(font=('Garamond', 18))
e4 = Entry(myw, bg='#d68f42')
e4.place(x=1050, y=300)
e4.config(font=('Garamond', 18))

myvar1 = IntVar()
myvar2 = IntVar()
myvar3 = IntVar()
myvar4 = IntVar()
myvar5 = IntVar()
myvar6 = IntVar()
lb5 = Label(myw, text="Select Gender", bg='#605691')
lb5.place(x=60, y=400)
lb5.config(font=('Garamond', 18))
rb1 = Radiobutton(myw, text="Male", variable=myvar1, value=0,
                  width=15, anchor='w', bg='#d68f42')
rb1.place(x=400, y=400)
rb1.config(font=('Garamond', 18))
rb2 = Radiobutton(myw, text="Female", variable=myvar1,
                  value=1, width=15, anchor='w', bg='#d68f42')
rb2.place(x=750, y=400)
rb2.config(font=('Garamond', 18))
rb3 = Radiobutton(myw, text="Transgender", variable=myvar1,
                  value=2, width=15, anchor='w', bg='#d68f42')
rb3.place(x=1100, y=400)
rb3.config(font=('Garamond', 18))


f1 = Frame(myw)
f1.place(x=400, y=500)
lb5 = Label(myw, text="Select Doctor", bg='#605691')
lb5.place(x=60, y=500)
lb5.config(font=('Garamond', 18))
cb1 = Checkbutton(f1, text="Cardiologist", variable=myvar2,
                  onvalue=100, offvalue=0, width=15, anchor='w', bg='#d68f42')
cb1.grid(row=1)
cb1.config(font=('Garamond', 18))
cb2 = Checkbutton(f1, text="Audiologist", variable=myvar3,
                  onvalue=30, offvalue=0, width=15, anchor='w', bg='#d68f42')
cb2.grid(row=2)
cb2.config(font=('Garamond', 18))
cb3 = Checkbutton(f1, text="Dentist", variable=myvar4, onvalue=50,
                  offvalue=0, width=15, anchor='w', bg='#d68f42')
cb3.grid(row=3)
cb3.config(font=('Garamond', 18))
cb4 = Checkbutton(f1, text="Gynaecologist", variable=myvar5,
                  onvalue=60, offvalue=0, width=15, anchor='w', bg='#d68f42')
cb4.grid(row=4)
cb4.config(font=('Garamond', 18))
cb5 = Checkbutton(f1, text="Paediatrician", variable=myvar6,
                  onvalue=20, offvalue=0, width=15, anchor='w', bg='#d68f42')
cb5.grid(row=5)
cb5.config(font=('Garamond', 18))


def enter(t):
    query = "INSERT into appointment(fname,lname,phone,age,gender,doctor) values(%s,%s,%s,%s,%s,%s)"
    val = (t[0], t[1], t[2], t[3], t[4], t[5])
    mycursor.execute(query, val)
    mycursor.execute("SELECT * FROM appointment")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    mydb.commit()


def submit():
    a = e2.get()
    b = e6.get()
    c = str(e3.get())
    d = str(e4.get())
    if myvar1.get() == 0:
        e = "Male"
    if myvar1.get() == 1:
        e = "Female"
    if myvar1.get() == 2:
        e = "Transgender"
    if myvar2.get() != 0:
        f = "Cardiologist"
    if myvar3.get() != 0:
        f = "Audiologist"
    if myvar4.get() != 0:
        f = "Dentist"
    if myvar5.get() != 0:
        f = "Gynaecologist"
    if myvar6.get() != 0:
        f = "Paediatrician"
    val = (a, b, c, d, e, f)
    enter(val)
    lb7 = Label(myw, text=val, bg='light green')
    lb7.place(x=900, y=700)
    lb7.config(font=('Garamond', 12))


btn1 = Button(myw, text="Submit Details", command=submit, bg='#b0d18a')
btn1.config(font=('Garamond', 18))
btn1.place(x=1000, y=600)


btn2 = Button(myw, text="Go To Home Page", command=myw.destroy, bg='teal')
btn2.config(font=('Garamond', 18))
btn2.place(x=60, y=600)
mainloop()
