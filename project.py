import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


nama = []
jadwal = []


root = tk.Tk()
root.title("Aplikasi Jadwal")
root.geometry("400x400")


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
b1 = Button(bFrame,  text="Tambah")
b1.grid(row=0, column=0)
b2 = Button(bFrame, text="Edit")
b2.grid(row=0, column=1)
b3 = Button(bFrame, text="Delete")
b3.grid(row=0, column=2)


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

tabel.insert(parent='',index='end',iid=0,text='', values=('Tom','Senin'))
tabel.pack()


#FUNGSI
def tambah():
    datanama = name_entry.get()
    datahari = day_entry.get()

root.mainloop()