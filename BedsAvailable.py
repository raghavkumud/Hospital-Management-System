import tkinter
from tkinter import *
import Database
myw = Tk()
myw.configure(bg='#341adb')
myw.geometry('800x600')
# myw.state('zoomed')
all_full = True
ward_a = ""
room_no_ = 0
Database.cursor = Database.conn.cursor(buffered=True)

def check():
    global ward_a
    global room_no_
    global all_full
    q = f"select * from rooms"
    Database.cursor.execute(q)
    print(Database.cursor)
    for j in Database.cursor:
        if j[2] < 25:
            ward_a = j[0]
            room_no_ = j[2]+1
            all_full = False
            qr1 = f"update rooms set filled_= {j[2]+1} where ward='{ward_a}'"
            qr2 = f"update rooms set empty_= {j[3]-1} where ward='{ward_a}'"
            Database.cursor.execute(qr1)
            Database.cursor.execute(qr2)
            break
        else:
            continue
    Database.conn.commit()


lb1 = Label(myw, height=5, width=50, bg='orange')
lb1.grid(row=0, column=2,padx=15)
lb1.config(font=('Playfair Display', 18, 'bold'))


def disable():
    global btn1
    btn1.configure(state='disabled')


def beds():
    check()
    disable()
    if all_full == False:
        text = f"BEDS ARE AVAILABLE \n Ward {ward_a} is allocated to you and room no is {room_no_}."
        lb1.config(text=text)
    else:
        text = 'We are deeply sad to inform you that beds are not availabe.'
        lb1.config(text=text)


btn1 = Button(myw, text="Check Here", border=5, command=beds,
              bg='grey', font=('Playfair Display', 20))

btn1.grid(row=6, column=2)

mainloop()
