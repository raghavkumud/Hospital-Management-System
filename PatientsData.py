# Patients Data
import mysql.connector
import tkinter
from tkinter import *

myw = Tk()
myw.configure(bg='#341adb')
myw.geometry('1500x750')
myw.title('Patients Data')
myw.state('zoomed')

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="proca213")
mycursor = mydb.cursor()
# mycursor.execute("Create Database mydatabase")
# sql = "Drop Table IF exists patient"
# mycursor.execute(sql)
# mycursor.execute("Create table patient(fname VARCHAR(50),lname VARCHAR(50),phone int,age int, gender varchar(20),ward varchar(50),room varchar(50))")


a = ""
b = ""
c = ""
d = ""
e = ""
f = ""

lb1 = Label(myw, text="Patients Booking Detail", bg='orange')
lb1.grid(row=0, column=1,padx=50,pady=30)
lb1.config(font=('Playfair Display', 20))

lb2 = Label(myw, text="First Name:", bg='light green')
lb2.grid(row=1, column=0,padx=40,pady=5,sticky='WE')
lb2.config(font=('Playfair Display', 18))
e2 = Entry(myw, bg='light blue')
e2.grid(row=1, column=1,padx=40,pady=5,sticky='WE')
e2.config(font=('Playfair Display', 18))

lb6 = Label(myw, text="Last Name:", bg='light green')
lb6.grid(row=2, column=0,padx=40,pady=5,sticky='WE')
lb6.config(font=('Playfair Display', 18))
e6 = Entry(myw, bg='light blue')
e6.grid(row=2, column=1,padx=40,pady=5,sticky='WE')
e6.config(font=('Playfair Display', 18))

lb3 = Label(myw, text="Phone Number:", bg='light green')
lb3.grid(row=3, column=0,padx=40,pady=5,sticky='WE')
lb3.config(font=('Playfair Display', 18))
e3 = Entry(myw, bg='light blue')
e3.grid(row=3, column=1,padx=40,pady=5,sticky='WE')
e3.config(font=('Playfair Display', 18))

lb4 = Label(myw, text="Age:", bg='light green')
lb4.grid(row=4, column=0,padx=40,pady=5,sticky='WE')
lb4.config(font=('Playfair Display', 18))
e4 = Entry(myw, bg='light blue')
e4.grid(row=4, column=1,padx=40,pady=5,sticky='WE')
e4.config(font=('Playfair Display', 18))

myvar1 = IntVar()
myvar2 = IntVar()
fr1 = Frame(myw,bg='light green')
fr1.grid(row=5, column=0,padx=40,pady=5)
lb5 = Label(fr1, text="Select Gender:", bg='light green')
lb5.grid(row=0, column=0,padx=10,pady=3)
lb5.config(font=('Playfair Display', 18))

rb1 = Radiobutton(fr1, text="Male", variable=myvar1,
                  value=0, width=15, anchor='w', bg='blue')
rb1.grid(row=1, column=1,padx=3,pady=3)
rb1.config(font=('Playfair Display', 18))
rb2 = Radiobutton(fr1, text="Female", variable=myvar1,
                  value=1, width=15, anchor='w', bg='pink')
rb2.grid(row=2, column=1,padx=3,pady=3)
rb2.config(font=('Playfair Display', 18))
rb3 = Radiobutton(fr1, text="Transgender", variable=myvar1,
                  value=2, width=15, anchor='w', bg='orange')
rb3.grid(row=3, column=1,padx=3,pady=3)
rb3.config(font=('Playfair Display', 18))

fr2 = Frame(myw,bg='light green')
fr2.grid(row=6, column=0,padx=40,pady=5,sticky='WE')
lb6 = Label(fr2, text="Select Ward:", bg='light green')
lb6.grid(row=0, column=0,padx=10,pady=3)
lb6.config(font=('Playfair Display', 18))
rb4 = Radiobutton(fr2, text="Ward A", variable=myvar2,
                  value=0, width=10, anchor='w', bg='teal')
rb4.grid(row=1, column=1,padx=3,pady=3)
rb4.config(font=('Playfair Display', 18))
rb5 = Radiobutton(fr2, text="Ward B", variable=myvar2,
                  value=1, width=10, anchor='w', bg='violet')
rb5.grid(row=2, column=1,padx=3,pady=3)
rb5.config(font=('Playfair Display', 18))
rb6 = Radiobutton(fr2, text="Ward C", variable=myvar2,
                  value=2, width=10, anchor='w', bg='cyan')
rb6.grid(row=3, column=1,padx=3,pady=3,sticky='WE')
rb6.config(font=('Playfair Display', 18))
rb7 = Radiobutton(fr2, text="Ward D", variable=myvar2,
                  value=3, width=10, anchor='w', bg='purple')
rb7.grid(row=4, column=1,padx=3,pady=3)
rb7.config(font=('Playfair Display', 18))

lb8 = Label(myw, text="Enter Room Number Alloted:", bg='light green')
lb8.grid(row=7, column=0,padx=40,pady=5,sticky='WE')
lb8.config(font=('Playfair Display', 18))
e8 = Entry(myw, bg='light blue')
e8.grid(row=7, column=1,padx=40,pady=5,sticky='WE')
e8.config(font=('Playfair Display', 18))


def enter(a):
    query = "INSERT INTO patient(fname,lname,phone,age,gender,ward,room) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    val = (a[0], a[1], a[2], a[3], a[4], a[5], a[6])
    mycursor.execute(query)
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
    if myvar2.get() == 0:
        f = "A"
    if myvar2.get() == 1:
        f = "B"
    if myvar2.get() == 2:
        f = "C"
    if myvar2.get() == 3:
        f = "D"
    g = str(e8.get())
    val = (a, b, c, d, e, f, g)
    # print(val)
    query = "INSERT INTO patient(fname,lname,phone,age,gender,ward,room) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query, val)
    mycursor.execute("SELECT * FROM appointment")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    lb7 = Label(myw, text="Name = "+a+" "+b+", Number = "+" "+c+", Age = " +
                d+", Gender = "+e+", Ward = "+f+", Room = "+g, bg='light green')
    lb7.grid(row=8, column=2)
    lb7.config(font=('Playfair Display', 20))


btn1 = Button(myw, text="Submit Details", command=submit, bg='aqua')
btn1.config(font=('Playfair Display', 18))
myw.columnconfigure(6,weight=1)
btn1.grid(row=10, column=7,padx=40,pady=10)

mainloop()
