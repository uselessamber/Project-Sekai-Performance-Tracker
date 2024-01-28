def scoring_system(perfect : int, 
                   great   : int, 
                   good    : int, 
                   bad     : int, 
                   miss    : int):
    note_count = perfect + great + good + bad + miss
    note_score = 10000000 / note_count
    return int((note_score + 1) * perfect + (note_score * 0.5) * great)

def score_modifier(score : int):
    if score >= 10000000:
        return 2.0
    elif score >= 9800000:
        return 1.0 + (score - 9800000) / 200000
    else:
        return (score - 9500000) / 300000

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
        self.data["score"] = scoring_system(
            self.data["perfect"],
            self.data["great"],
            self.data["good"],
            self.data["bad"],
            self.data["miss"]
        )
        if self.data["score"] >= 9900000:
            self.data["rank"] = "EX+"
        elif self.data["score"] >= 9800000:
            self.data["rank"] = "EX"
        elif self.data["score"] >= 9500000:
            self.data["rank"] = "AA"
        elif self.data["score"] >= 9200000:
            self.data["rank"] = "A"
        elif self.data["score"] >= 8900000:
            self.data["rank"] = "B"
        elif self.data["score"] >= 8600000:
            self.data["rank"] = "C"
        else:
            self.data["rank"] = "D"
        self.data["p-rating"] = self.data["diff"] + score_modifier(self.data["score"])