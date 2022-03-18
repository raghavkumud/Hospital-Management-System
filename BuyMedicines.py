from tkinter import *
import tkinter.font as tkFont
import Database
mw = Tk()
font_ = tkFont.Font(family='PT Mono',size=20,weight='bold')
#Database.check_info(Database.cursor)
mw.geometry('800x400')
mw.configure(bg='#6146a6')
#mw.state('zoomed')
fr2 = Frame(mw)
fr2.grid(row=1,column=1,padx=20,pady=30)
listbox = Listbox(fr2, width=60, height=16, selectmode=MULTIPLE,bg="#638791")
listbox.insert(1, "Azithromycin")
listbox.insert(2, "Chloroquine Phosphate")
listbox.insert(3, "Malorone")
listbox.insert(4, "Vibramycin")
listbox.insert(5, "Acetaminophen")
listbox.insert(6, "Ibuprofen")
listbox.insert(7, "Paracetamol")
listbox.insert(8, "Chlorothiazide")
listbox.insert(9, "Chlorthalidone")
listbox.insert(10, "Amlodipine")
listbox.insert(11, "Benazepril")
listbox.insert(12, "Acebutolol")
listbox.insert(13, "Amiloride")
listbox.insert(14, "Rifaximin")
listbox.insert(15, "Rifamycin")
listbox.insert(16, "Ciprofloxacin")
lb1 = Label(fr2,height=5,width=50,bg='orange')
lb1.grid(row=0,column=2,padx=20)
def get_items():
     
    lis = []
    for i in listbox.curselection():
        lis.append(listbox.get(i))
    tp=0
    listbox.selection_clear(0,int(listbox.size()-1))
    lis_stock_out=[]
    Database.cursor = Database.conn.cursor()
    for i in lis:
        query = f"select price,quantity,name from medicines where name='{i}'"
        print(query)
        Database.cursor.execute(query)
        for j in Database.cursor:
            val = j[0]
            tp+=val
            qval = j[1]
            if qval < 100:
                lis_stock_out.append(j[2])
            else:
                tp+=val
                qval-=5
                query_2 = f"update medicines set quantity = {qval} where name = '{j[2]}'"
                print(query_2)
                Database.cursor.execute(query_2)  
            
        Database.conn.commit()     

    rs = u"\u20B9"
    if len(lis_stock_out)==0:

        lb1.config(text=f"You need to pay {rs}{tp:.2f} only.")
    else:
        ss = 'Sorry these medicines are out of stock'
        yy=""
        for i in range(len(lis_stock_out)):
            if i==len(lis_stock_out)-1:
                yy+=lis_stock_out[i]
            else:
                yy+=lis_stock_out[i]
                yy+=","
        fs = f"{ss} : {yy} \n You need to pay {rs}{tp:.2f} only for rest of the medicines."
        lb1.config(text=fs)
    

btn = Button(fr2, text='Buy',bg='cyan' ,command=get_items)

btn.grid(row=2,column=0)
listbox.grid(row=0,column=0)
mainloop()