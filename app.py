import tksheet as tks
import tkinter as tk
import library
from library.database_interface import db_interface

if __name__ == "__main__":
    master = tk.Tk()
    master.iconbitmap("app.ico")
    master.title("Project Sekai Performance Tracker v1.12")
    app = db_interface(master)
    app.mainloop()
