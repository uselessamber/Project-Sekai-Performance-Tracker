# The Project Sekai Performance Tracker
![UI Showcase](https://i.imgur.com/gsHOfq2.png)
## I. What is this?
This program helps keep track of your performance in a mobile rhythm game called Project Sekai.
Sadly, outside of ranked play in that game, the score is calculated by a combination of several factors with minimal dependency on accuracy. In other word, outside of ranked play, PJSK does not have an accuracy based scoring system. It annoys me a lot so I have decided to take it upon myself to make a program that keep tracks of approximately how good you are at the game.

The v1 version of this program uses the precise version of Arcaea's scoring system. Which after a bit of calculation turns out to be not as good as I thought. Elaborate down in the play rating section.

The v3 version completely phased out Arcaea's scoring system entirely in favor of its own system based on the ranked score (Score which you would get by playing this chart in ranked matches) for a more accurate performance tracking.

## II. Scoring System
The scoring uses the same system as Project Sekai Ranked Score
The score are calculated as:
- Perfect notes = 3
- Great notes = 2
- Good notes = 1
- Bad and Misses = 0
The ranking is calculated based on your accuracy:
- SS+ <-- Accuracy == 100%
- SS  <-- 99% <= Accuracy < 100%
- S   <-- 97% <= Accuracy < 99%
- A   <-- 92% <= Accuracy < 97%
- B   <-- 85% <= Accuracy < 92%
- C   <-- 76% <= Accuracy < 85%
- F   <-- Accuracy < 76%

## III. Play rating
To calculate the play rating, the accuracy is converted to score modifier using the equation below:
- For 100% accuracy         : *3.0*
- For accuracy above 97%    : score_modifier = 1 + (2 * (accuracy - 97) / 3)
- Other                     : score_modifier = 1 * ((accuracy - 92) / 5)
Then the score modifier is added to the difficulty to get the play rating, which is used for the Overall Rating system.

## IV. Rating calculation
Internally, scores are saved in 2 different files:
- Global play, which keep track of every score you have.
- Recent play, which keep track of the last 10 scores you got.
To calculate the potential, the top 30 score (dictated by play ratings) are taken into account alongside the last 10 scores you got.
The calculation is: (Sg + Sr) / 40
With:
- Sg = The sum of the top 30 play ratings.
- Sr = The sum of the last 10 play ratings you have.

## V. What will be added in the future?
Song list has been implemented.
Song sorting has been implemented.
Song list is malleable and can be modified to update new songs (within the song_list folder).
Probably automatic difficulty setting, support for Append difficulty and JP server in the future.