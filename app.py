import tksheet as tks
import tkinter as tk
import tkinter.ttk as ttk
import library
from library.database_interface import db_interface

if __name__ == "__main__":
    master = tk.Tk()
    master.iconbitmap("app.ico")
    master.title("Project Sekai Performance Tracker v2")
    style = ttk.Style(
        master = master
    )
    style.theme_use("vista")
    app = db_interface(master)
    app.mainloop()
