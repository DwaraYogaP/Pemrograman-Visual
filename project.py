import tkinter as tk

master = tk.Tk()
master.title("Aplikasi Jadwal")
master.geometry("300x300")
master.iconbitmap('icon.ico')

tk.Label(master, text="Aplikasi Jadwal").grid(row=0, column=1)
tk.Button(master, text="Buat Jadwal").grid(row=2, column=1)
tk.Label(master, text="").grid(row=3, column=1)
tk.Button(master, text="Lihat Jadwal").grid(row=4, column=1)
tk.Label(master, text="").grid(row=5, column=1)
tk.Button(master, text="Edit Jadwal").grid(row=6, column=1)
tk.Label(master, text="").grid(row=7, column=1)
tk.Button(master, text="Hapus Jadwal").grid(row=8, column=1)
tk.Label(master, text="").grid(row=9, column=1)
tk.Button(master, text="Keluar").grid(row=10, column=1)


tk.mainloop()