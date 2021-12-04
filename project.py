import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
import tkinter.ttk as ttk

class Orang:
    nama = ''
    hari = ''

dataJadwal = []

OPTIONS = [
        "Senin",
        "Selasa",
        "Rabu",
        "Kamis",
        "Jumat",
        "Sabtu",
        "Minggu"
        ]


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("500x500")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Aplikasi Jadwal Piket", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Buat Jadwal",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Lihat Jadwal",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Edit Jadwal",
                            command=lambda: controller.show_frame("PageThree"))
        button4 = tk.Button(self, text="Hapus Jadwal",
                            command=lambda: controller.show_frame("PageFour"))
        
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Buat Jadwal", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        nama = tk.Label(self, text = "Nama Lengkap")      
        e1 = tk.Entry(self, width = 40)
        nama.place(x = 20, y = 50)      
        e1.place(x = 20, y = 70)

        jadwal = tk.Label(self, text = "Jadwal")
        jadwal.place(x = 20, y = 100)
        

        variable = StringVar()
        variable.set(OPTIONS[0])

        w = OptionMenu(self, variable, *OPTIONS)
        w.place(x = 20, y = 120)
            
                
        kirim = tk.Button(self, text="Kirim", command=submit(w, e1))
        kirim.place(x = 20, y = 180)

        button = tk.Button(self, text="Kembali", command=lambda: controller.show_frame("StartPage"))
        button.place(x = 100, y = 180)
        

# https://pythonguides.com/python-tkinter-table-tutorial/
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Lihat Jadwal", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        tabel = ttk.Treeview(self)
        tabel['columns'] = ('NAMA', 'HARI')

        tabel.column("#0", width=0,  stretch=NO)
        tabel.column("NAMA",anchor=CENTER, width=80)
        tabel.column("HARI",anchor=CENTER,width=80)

        tabel.heading("#0",text="",anchor=CENTER)
        tabel.heading("NAMA",text="NAMA",anchor=CENTER)
        tabel.heading("HARI",text="HARI",anchor=CENTER)
        
        for data in dataJadwal:
            val = 0
            if dataJadwal is None:
                tabel.insert(parent='', index='end', iid=val, text='', values=(''))
            else:
                tabel.insert(parent='', index='end', iid=val, text='', values=(data.nama, data.hari))
            tabel.pack()

        

        button = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Edit Jadwal", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hapus Jadwal", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

def submit(OPTIONS, e1):
    data = Orang()
    if OPTIONS == "Senin":
        data.nama = e1
        data.hari = "Senin"
        dataJadwal.append(data)
    elif OPTIONS == "Selasa":
        data.nama = e1
        data.hari = "Selasa"
        dataJadwal.append(data)
    elif OPTIONS == "Rabu":
        data.nama = e1
        data.hari = "Rabu"
        dataJadwal.append(data)
    elif OPTIONS == "Kamis":
        data.nama = e1
        data.hari = "Kamis"
        dataJadwal.append(data)
    elif OPTIONS == "Jumat":
        data.nama = e1
        data.hari = "Jumat"
        dataJadwal.append(data)
    elif OPTIONS == "Sabtu":
        data.nama = e1
        data.hari = "Sabtu"
        dataJadwal.append(data)
    else:
        data.nama = e1
        data.hari = "Minggu"
        dataJadwal.append(data)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()