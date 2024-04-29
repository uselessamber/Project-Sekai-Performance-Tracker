def scoring_system(perfect : int, 
                   great   : int, 
                   good    : int, 
                   bad     : int, 
                   miss    : int):
    note_count = perfect + great + good + bad + miss
    score = perfect * 3 + great * 2 + good
    max_score = note_count * 3
    return (score, (((score / max_score) * 10000) // 1) / 100)

def score_modifier(accuracy : int):
    if accuracy >= 100:
        return 3.0
    elif accuracy >= 97:
        return 1 + 2 * ((accuracy - 97) / 3)
    else:
        return 1 * ((accuracy - 92) / 5)

class song:
    def __init__(self, 
                 song_name : str, 
                 song_difficulty : int, 
                 notes : list[int]): # perfect, great, good, bad, miss
        self.data = {
            "name"     : song_name,
            "diff"     : song_difficulty,
            "perfect"  : notes[0],
            "great"    : notes[1],
            "good"     : notes[2],
            "bad"      : notes[3],
            "miss"     : notes[4],
            "score"    : 0,
            "accuracy" : 0,
            "rank"     : "D",
            "p-rating" : 0
        }
        self.update_score()

    def update_notes(self,
                     perfect : int,
                     great : int,
                     good : int,
                     bad : int,
                     miss : int):
        if scoring_system(perfect, great, good, bad, miss) > self.data["score"]:
            self.data["perfect"] = perfect
            self.data["great"]   = great
            self.data["good"]    = good
            self.data["bad"]     = bad
            self.data["miss"]    = miss
            self.update_score()

    def update_score(self):
        self.data["score"], self.data["accuracy"] = scoring_system(
            self.data["perfect"],
            self.data["great"],
            self.data["good"],
            self.data["bad"],
            self.data["miss"]
        )
        if   self.data["accuracy"] >= 100:
            self.data["rank"] = "SS+"
        elif self.data["accuracy"] >= 99:
            self.data["rank"] = "SS"
        elif self.data["accuracy"] >= 97:
            self.data["rank"] = "S"
        elif self.data["accuracy"] >= 92:
            self.data["rank"] = "A"
        elif self.data["accuracy"] >= 85:
            self.data["rank"] = "B"
        elif self.data["accuracy"] >= 76:
            self.data["rank"] = "C"
        else:
            self.data["rank"] = "F"
        self.data["p-rating"] = self.data["diff"] + score_modifier(self.data["accuracy"])