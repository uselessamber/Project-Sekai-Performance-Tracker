import json
from library.song import *

class song_database:
    def __init__(self):
        self.song_list = []
        self.recent_play = []

    def save_data(self):
        with open("play_data/global_play.json", "w+") as f:
            output = []
            for s in self.song_list:
                output.append(s.data)
            json.dump(output, f)

        with open("play_data/recent_play.json", "w+") as f:
            output = []
            for s in self.recent_play:
                output.append(s.data)
            json.dump(output, f)
    
    def load_data(self):
        try:
            with open("play_data/global_play.json", "r+") as f:
                temp_list = json.load(f)
                for obj in temp_list:
                    self.song_list.append(song(
                        obj["name"],
                        obj["diff"],
                        [
                            obj["perfect"],
                            obj["great"],
                            obj["good"],
                            obj["bad"],
                            obj["miss"],
                        ]
                    ))
        except OSError:
            print("Global save file does not exist.")

        try:
            with open("play_data/recent_play.json", "r+") as f:
                temp_list = json.load(f)
                for obj in temp_list:
                    self.recent_play.append(song(
                        obj["name"],
                        obj["diff"],
                        [
                            obj["perfect"],
                            obj["great"],
                            obj["good"],
                            obj["bad"],
                            obj["miss"],
                        ]
                    ))
        except OSError:
            print("Recent save file does not exist.")
    
    def find_global_song(self, song_name : str):
        for idx, s in enumerate(self.song_list):
            if s.data["name"] == song_name:
                return idx
        return None
    
    def find_recent_song(self, song_name : str):
        for idx, s in enumerate(self.recent_play):
            if s.data["name"] == song_name:
                return idx
        return None

    def add_data(self, 
                    song_name : str,
                    difficulty : int,
                    perfect : int, 
                    great : int, 
                    good : int, 
                    bad : int, 
                    miss : int):
        position = self.find_global_song(song_name)
        if position is not None:
            self.song_list[position].update_notes(perfect,
                                                  great,
                                                  good,
                                                  bad,
                                                  miss)
        else:
            self.song_list.append(song(song_name, difficulty, [perfect, great, good, bad, miss]))
        
        position = self.find_recent_song(song_name)
        if position is not None:
            self.recent_play[position].update_notes(perfect,
                                                  great,
                                                  good,
                                                  bad,
                                                  miss)
        else:
            self.recent_play.append(song(song_name, difficulty, [perfect, great, good, bad, miss]))
            if len(self.recent_play) > 10:
                self.recent_play.pop(0)

    def sort_by(self, s_type, descending_order = False):
        type_list = [
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
        if s_type in type_list:
            if s_type == "name":
                return sorted(self.song_list, 
                                        key = lambda d : d.data[s_type].upper(), 
                                        reverse = descending_order)
            return sorted(self.song_list, 
                                    key = lambda d : d.data[s_type], 
                                    reverse = descending_order)
    
    def get_top_play_rating(self, amount : int = 30):
        output = []
        temp_list = self.sort_by("p-rating")
        for i in range(min(len(temp_list), amount)):
            output.append(temp_list[i].data["p-rating"])
        return output
    
    def get_recent_play_rating(self):
        output = []
        for i in range(len(self.recent_play)):
            output.append(self.recent_play[i].data["p-rating"])
        return output

    def get_potential(self, top_play_range : int = 30):
        top_rating = sum(self.get_top_play_rating(top_play_range))
        recent_rating = sum(self.get_recent_play_rating())
        return (top_rating + recent_rating) / (top_play_range + 10)
