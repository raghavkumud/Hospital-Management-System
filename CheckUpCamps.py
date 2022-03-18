from tkinter import *
import tkinter.font as tkFont
import Database
mw = Tk()
font_ = tkFont.Font(family='Garamond', size=20, weight='bold')
font_i = tkFont.Font(family='Arial', size=12, weight='bold', slant='italic')
# Database.check_info(Database.cursor)
mw.geometry('800x400')
mw.configure(bg='#191970')
# mw.state('zoomed')
fr1 = Frame(mw, bg='#eeff77')
fr1.grid(row=2, column=2,padx=40,pady=20)
lb1 = Label(fr1, text=Database.infs, bg='#13dcf2', font=font_)
lb1.grid(row=0, column=2,padx=140,pady=20)


def cw():
    win = Tk()
    win.geometry('1000x450')
    win.configure(bg='#1a1ac4')
    info_s = Database.all_events(Database.cursor)
    st = ''
    for i in info_s:
        st += i
        st += '\n'

    lb1 = Label(win, text=st, bg='#e88331')
    lb1.config(font=font_i)
    print(st)
    lb1.grid(row=2, column=2)
    mainloop()


bt1 = Button(fr1, text="Click for more information", command=cw, font=font_)
bt1.grid(row=4, column=2)
mainloop()
