import tkinter as tk

master = tk.Tk()
master.title("Pemrograman Visual")
master.geometry("300x300")

tk.Label(master, text="Project Pemrograman Visual").grid(row=0, column=0)
tk.Button(master, text="Tombol 1").grid(row=1, column=0)
tk.Button(master, text="Tombol 2").grid(row=1, column=1)
tk.Label(master, text="P").grid(row=2, column=0)

tk.mainloop()