# Main

import tkinter
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image 
def cw():

    import CheckUpCamps as ff
	
def get_items():

    import BuyMedicines as cc
#main window
myw=tk.Tk()
myw.geometry('1400x960')
myw.title("Project HMS")
myw.state('zoomed')
myw.configure(bg="#9999ff")
# Image Part
myimage=Image.open(".\images\Doctor.jpg")
myimage=myimage.resize((600,400)) #pass width and height as tuple data type
img=ImageTk.PhotoImage(myimage)
label=tk.Label(myw,image=img)
label.grid(row=1,column=2)

fr1 = Frame(myw,bg="#e6f2ff")
fr1.grid(row=5,column=1,padx=50,pady=50)
fr2 = Frame(myw,bg="#e6f2ff")
fr2.grid(row=5,column=3,padx=50,pady=50)


# Functional Part   

lb1=Label(myw,text="Hospital Management System",font=('Playfair Display',20))
lb1.grid(row=0,column=2,pady=20) #padx and pady are external paddings

def Apt():
    	import Appointment   	

def bed_available():
	import BedsAvailable
def patient():
	import PatientsData


# execfile('Appointment.py')
# frame 1 for user part two buttons one for booking appointment other for checking free check up camps available
btn1 = Button(fr1,text ="Book An Appointment",command = Apt,bg='#6d8f42')
btn1.config(font=('Playfair Display',16))
btn1.grid(row=0,column=0)
btn2 = Button(fr1,text ="Buy Medicines",command = get_items,bg='#6d8f42')
btn2.config(font=('Playfair Display',16))
btn2.grid(row=1,column=0)
btn3 = Button(fr1,text ="Check Free Check Up Camps Organised",command = cw,bg='#6d8f42')
btn3.config(font=('Playfair Display',16))
btn3.grid(row=2,column=0)
# frame 2 for admin role
btn4 = Button(fr2,text ="Admit A Patient",command = patient,bg='#6d8f42')
btn4.config(font=('Playfair Display',16))
btn4.grid(row=0,column=0)
#btn5 = Button(fr2,text ="Manage Stock of Medicines",bg='#6d8f42')
#btn5.config(font=('Playfair Display',16))
#btn5.grid(row=1,column=0)
btn6 = Button(fr2,text ="Check Beds Available",command = bed_available,bg='#6d8f42')
btn6.config(font=('Playfair Display',16))
btn6.grid(row=2,column=0)

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="abc_xyz21",database="proca213")
mycursor = mydb.cursor()
'''val=("keshav","Vyas",19,16,"Male","Dentist")
query="INSERT into appointment(fname,lname,phone,age,gender,doctor) values(%s,%s,%s,%s,%s,%s)"
mycursor.execute(query,val)'''

mainloop()