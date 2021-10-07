import tkinter as tk

master = tk.Tk()
master.title("Aplikasi Jadwal")
master.geometry("300x300")

tk.Label(master, text="Aplikasi Jadwal").grid(row=0, column=0)
tk.Button(master, text="Buat Jadwal").grid(row=1, column=0)
tk.Button(master, text="Lihat Jadwal").grid(row=2, column=0)
tk.Button(master, text="Edit Jadwal").grid(row=3, column=0)
tk.Button(master, text="Hapus Jadwal").grid(row=4, column=0)
tk.Button(master, text="Keluar").grid(row=5, column=0)


tk.mainloop()