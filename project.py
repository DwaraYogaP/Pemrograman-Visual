import tkinter as tk

master = tk.Tk()
master.title("Pemrograman Visual")
master.geometry("300x300")

tk.Label(master, text="Project Pemrograman Visual").grid(row=0, column=0)
tk.Button(master, text="Tombol").grid(row=1, column=0)


tk.mainloop()