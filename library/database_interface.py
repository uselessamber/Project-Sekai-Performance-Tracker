from library.song import *
from library.song_database import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tksheet as tks

class NoDataError(Exception):
    pass

allowed_song_list = []
allowed_difficulty_list = ["Easy", "Normal", "Hard", "Expert", "Master"]
allowed_sort_type = [
            "name", 
            "diff", 
            "perfect", 
            "great",
            "good",
            "bad",
            "miss",
            "score",
            "rank",
            "p-rating"]

class db_interface(tk.Frame):
    def open_song_list(self):
        global allowed_song_list
        with open("song_list/song_name.txt", "r+", encoding = "utf-8") as f:
            for line in f.readlines():
                while line[-1] == "\n" or line[-1] == " ":
                    line = line[:-1]
                allowed_song_list.append(line)
        allowed_song_list.sort(key = lambda v : v.upper())
    
    def __init__(self, master = None, width = 1250, height = 900):
        self.open_song_list()

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
            font   = ("Aptos", 26), 
            text   = f"Potential\n{self.potential:.02f}")
        self.potential_label.pack()

        # Save Data
        self.save_button = tk.Button(
            master  = self.main_frame,
            font    = ("Aptos", 14),
            text    = "Save Data",
            command = self.data_save
        )
        self.save_button.pack()

        # Sorting Frame
        self.sort_frame = tk.Frame(self.main_frame, width = width)
        self.sort_frame.pack()

        self.sort_combobox = ttk.Combobox(
            master = self.sort_frame,
            font   = ("Times New Roman", 12),
            state  = "readonly",
            values = allowed_sort_type
        )
        self.sort_combobox.grid(row = 0, column = 0)

        self.sort_button = tk.Button(
            master = self.sort_frame,
            font    = ("Aptos", 12),
            text    = "Sort Data",
            command = self.sort_data
        )
        self.sort_button.grid(row = 0, column = 1)

        self.is_descending = tk.BooleanVar()
        self.sort_descending = tk.Checkbutton(
            master   = self.sort_frame,
            font     = ("Times New Roman", 14), 
            text     = f"Descending",
            variable = self.is_descending,
            onvalue  = True,
            offvalue = False
        )
        self.sort_descending.grid(row = 0, column = 2)

        # List all available data
        self.song_display = tks.Sheet(self.main_frame, width = width)
        self.table_update()
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
            font   = ("Times New Roman", 14), 
            text   = f"Insert / Modify a song below"
        )
        self.potential_input_label.pack()

        # Adding data fields
        self.second_frame = tk.Frame(self.main_frame, width = width, height = height)
        self.second_frame.pack()

        labels = [
            "Song Name: ",
            "Difficulty: ",
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
                font   = ("Times New Roman", 12),
                text   = label,
            ))
            self.label_list[-1].grid(row = idx, column = 0, sticky = 'W', pady = 2)
            
            if idx == 0:
                self.input_list.append(ttk.Combobox(
                    master = self.second_frame,
                    font   = ("Times New Roman", 12),
                    state  = "readonly",
                    values = allowed_song_list
                ))
                self.input_list[-1].grid(row = idx, column = 1, sticky = 'E', pady = 2)
            elif idx == 1:
                self.input_list.append(ttk.Combobox(
                    master = self.second_frame,
                    font   = ("Times New Roman", 12),
                    state  = "readonly",
                    values = allowed_difficulty_list
                ))
                self.input_list[-1].grid(row = idx, column = 1, sticky = 'E', pady = 2)                
            else:
                self.input_list.append(tk.Entry(
                    master = self.second_frame,
                    font   = ("Times New Roman", 12)
                ))
                self.input_list[-1].grid(row = idx, column = 1, sticky = 'E', pady = 2)
        
        # Submit button
        self.submit_button = tk.Button(
            master  = self.main_frame,
            font    = ("Aptos", 14),
            text    = "Submit",
            command = self.write_data
        )
        self.submit_button.pack()

    def table_update(self):
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

    def sort_data(self):
        self.main_db.song_list = self.main_db.sort_by(self.sort_combobox.get(), self.is_descending.get())
        self.table_update()

    def data_save(self):
        self.main_db.save_data()
        self.table_update()
    
    def write_data(self):
        try:
            if self.input_list[0].get() == "" or self.input_list[1].get() == "":
                raise NoDataError
            song_name = self.input_list[0].get() + " [" + self.input_list[1].get() + "]"
            song_difficulty = int(self.input_list[2].get())
            note_count = [
                int(self.input_list[3].get()),
                int(self.input_list[4].get()),
                int(self.input_list[5].get()),
                int(self.input_list[6].get()),
                int(self.input_list[7].get())
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
            self.potential_label.config(text = f"Potential\n{self.potential:.02f}")
            
            for i in range(2, 8):
                self.input_list[i].delete(0, 'end')
            
            self.table_update()

        except NoDataError:
            messagebox.showerror(
                title = "Input Error",
                message = "No song / difficulty.",
            )
        except ValueError:
            messagebox.showerror(
                title = "Input Error",
                message = "Invalid Characters in text field.",
            )
