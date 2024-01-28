from library.song import *
from library.song_database import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tksheet as tks

class db_interface(tk.Frame):
    def __init__(self, master = None, width = 1000, height = 750):
        # Initialize screen
        super().__init__(master)
        self.master = master

        self.main_frame = tk.Frame(self.master, width = width, height = height)
        self.main_frame.pack()

        # Initialize database
        self.main_db = song_database()
        self.main_db.load_data()
        self.potential = self.main_db.get_potential()

        # Potential Display
        self.potential_label   = tk.Label(
            master = self.main_frame, 
            font   = ("Consolas", 26), 
            text   = f"Potential: {self.potential:.02f}")
        self.potential_label.pack()

        # Save Data
        self.save_button = tk.Button(
            master  = self.main_frame,
            font    = ("Consolas", 14),
            text    = "Save Data",
            command = self.data_save
        )
        self.save_button.pack()

        # List all available data
        self.song_display = tks.Sheet(self.main_frame, width = width)
        self.table = [
                [
                    "name", 
                    "diff", 
                    "perfect", 
                    "great",
                    "good",
                    "bad",
                    "miss",
                    "score",
                    "rank",
                    "p-rating"
                ]
            ]
        for s in self.main_db.song_list:
            self.table.append([s.data[t] for t in self.table[0]])
        self.song_display.set_sheet_data(self.table)
        self.song_display.enable_bindings((
            "copy",
            "arrowkeys",
            "single_select",
            "column_width_resize"
        ))
        self.song_display.pack(fill = 'y', expand = True)

        # Text
        self.potential_display = f"{self.potential:.02f}"
        self.potential_input_label   = tk.Label(
            master = self.main_frame, 
            font   = ("Consolas", 14), 
            text   = f"Insert / Modify a song below")
        self.potential_input_label.pack()

        # Adding data fields
        self.second_frame = tk.Frame(self.main_frame, width = width, height = height)
        self.second_frame.pack()

        labels = [
            "Song Name [Text difficulty]: ",
            "Number Difficulty: ",
            "Perfect count: ",
            "Great count: ",
            "Good count: ",
            "Bad count: ",
            "Miss count: "
        ]
        # Song name text / song name input
        self.label_list = []
        self.input_list = []
        for idx, label in enumerate(labels):
            self.label_list.append(tk.Label(
                master = self.second_frame,
                font   = ("Consolas", 12),
                text   = label,
            ))
            self.label_list[-1].grid(row = idx, column = 0, sticky = 'W', pady = 2)
            
            self.input_list.append(tk.Entry(
                master = self.second_frame,
                font   = ("Consolas", 12)
            ))
            self.input_list[-1].grid(row = idx, column = 1, sticky = 'E', pady = 2)
        
        # Submit button
        self.submit_button = tk.Button(
            master  = self.main_frame,
            font    = ("Consolas", 14),
            text    = "Submit",
            command = self.write_data
        )
        self.submit_button.pack()

    def data_save(self):
        self.main_db.save_data()
    
    def write_data(self):
        try:
            song_name = self.input_list[0].get()
            song_difficulty = int(self.input_list[1].get())
            note_count = [
                int(self.input_list[2].get()),
                int(self.input_list[3].get()),
                int(self.input_list[4].get()),
                int(self.input_list[5].get()),
                int(self.input_list[6].get())
            ]
            self.main_db.add_data(
                song_name,
                song_difficulty,
                note_count[0],
                note_count[1],
                note_count[2],
                note_count[3],
                note_count[4]
            )

            new_potential = self.main_db.get_potential()
            change = new_potential - self.potential
            if abs(change) < 0.01:
                messagebox.showinfo(
                    title = "Potential",
                    message = "-Keep-"
                )
            else:
                messagebox.showinfo(
                    title = "Potential",
                    message = f"{'+' if change > 0 else ''}{change:.02f}"
                )
            self.potential = new_potential
            self.potential_label.config(text = f"Potential: {self.potential:.02f}")
            
            for i in range(7):
                self.input_list[i].delete(0, 'end')

            self.table = [
                [
                    "name", 
                    "diff", 
                    "perfect", 
                    "great",
                    "good",
                    "bad",
                    "miss",
                    "score",
                    "rank",
                    "p-rating"
                ]
            ]
            for s in self.main_db.song_list:
                self.table.append([s.data[t] for t in self.table[0]])
            self.song_display.set_sheet_data(self.table)

        except ...:
            messagebox.showerror(
                title = "Input Error",
                message = "There is something wrong with your input.",
            )
