import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


#FUNGSI
def tambah():
    datanama = name_entry.get()
    datahari = day_entry.get()

    iid = 0
    while True:
        if tabel.insert(parent='', index='end', iid=iid,text='', values=(datanama, datahari)) == FALSE:
            iid += 1
            return iid
        else:
            tabel.insert(parent='', index='end', iid=iid,text='', values=(datanama, datahari))
            break
    

def pilih():
    select = tabel.focus()
    value = tabel.item(select, 'values')

    name_entry.delete(0, END)
    day_entry.delete(0, END)

    name_entry.insert(0, value[0])
    day_entry.insert(0, value[1])

def edit():
    select = tabel.focus()
    tabel.item(select,text="",values=(name_entry.get(),day_entry.get()))

    name_entry.delete(0, END)
    day_entry.delete(0, END)

def hapus():
    select = tabel.focus()

    tabel.delete(select)



root = tk.Tk()
root.title("Aplikasi Jadwal")
root.geometry("400x500")


#FORM
frame = Frame(root)
frame.pack(pady=20)

name= Label(frame,text = "Nama Lengkap")
name.grid(row=0,column=0 )
day = Label(frame,text="Hari")
day.grid(row=0,column=1)

name_entry= Entry(frame)
name_entry.grid(row= 1, column=0)
day_entry = Entry(frame)
day_entry.grid(row=1,column=1)



#BUTTON
bFrame = Frame(root)
bFrame.pack(pady = 20)
b1 = Button(bFrame,  text="Tambah", command=tambah)
b1.grid(row=0, column=0)
b2 = Button(bFrame, text="Edit", command=edit)
b2.grid(row=0, column=1)
b3 = Button(bFrame, text="Hapus", command=hapus)
b3.grid(row=0, column=2)
b4 = Button(bFrame, text="Pilih", command=pilih)
b4.grid(row=1, column=1)


#VIEW
frame = tk.Frame(root)
frame.pack()

tabel = ttk.Treeview(frame)

tabel['columns'] = ('nama', 'hari')

tabel.column("#0", width=0,  stretch=NO)
tabel.column("nama",anchor=CENTER, width=80)
tabel.column("hari",anchor=CENTER,width=80)

tabel.heading("#0",text="",anchor=CENTER)
tabel.heading("nama",text="Nama",anchor=CENTER)
tabel.heading("hari",text="Hari",anchor=CENTER)

tabel.insert(parent='', index='end', iid=0,text='', values=('Tom','Senin'))
tabel.pack()


root.mainloop()