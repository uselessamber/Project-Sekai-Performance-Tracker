# The Project Sekai Performance Tracker
![UI Showcase](https://i.imgur.com/gsHOfq2.png)
## I. What is this?
This program helps keep track of your performance in a mobile rhythm game called Project Sekai.
Sadly, outside of ranked play in that game, the score is calculated by a combination of several factors with minimal dependency on accuracy. In other word, outside of ranked play, PJSK does not have an accuracy based scoring system. It annoys me a lot so I have decided to take it upon myself to make a program that keep tracks of approximately how good you are at the game.

The v1 version of this program uses the precise version of Arcaea's scoring system. Which after a bit of calculation turns out to be not as good as I thought. Elaborate down in the play rating section.

## II. Scoring System
The maximum score is 10000000 + note count.
First the program determines the score for each notes:
    note_score = 10000000 / note_count
Then the score are calculated as:
- Perfect notes = note_score + 1
- Great notes = note_score * 0.5
- Good, Bad and Misses = 0
The score are ranked using Arcaea ranking system as well:
- EX+ <-- Score >= 9900000
- EX  <-- 9800000 <= Score < 9900000
- AA  <-- 9500000 <= Score < 9800000
- A   <-- 9200000 <= Score < 9500000
- B   <-- 8900000 <= Score < 9200000
- C   <-- 8600000 <= Score < 8900000
- D   <-- Score < 8600000

## III. Play rating
Because Project Sekai does not have internal difficulty (or that it isn't public information), unlike Arcaea's Chart Constant, the calculation will be a bit different, but it is basically the same thing.

To calculate the play rating, the score is converted to score modifier using the equation below:
- For scores above 10000000 : *5.0*
- For scores above  9800000 : score_modifier = 2.5 + (2.5 * (score - 9800000) / 200000)
- Other                     : score_modifier = 2.5 * ((score - 9500000) / 300000)
Then the score modifier is added to the difficulty to get the play rating, which is used for the Potential system.

Initially, the value used for scores above 10 mil is 2.0, and above 9.8 mil is 1.0, which makes the maximum potential achieveable is 35.5. While this isn't too bad, the goal of the potential / rating system is to estimate the best level for you to play at. In theory, your potential - 2 are levels where you can full combo at, and potential - 1 are levels where you can EX at (aka. at your play level). So I modified the number to scale the potential range up to make the maximum potential achievable is now 38.5, which is only achieved through AP-ing every songs from level 32 and upward + 4 level 31 of your choice. 

## IV. Potential calculation
Internally, scores are saved in 2 different files:
- Global play, which keep track of every score you have.
- Recent play, which keep track of the last 10 scores you got.
To calculate the potential, the top 30 score (dictated by play ratings) are taken into account alongside the last 10 scores you got.
The calculation is: (Sg + Sr) / 40
With:
- Sg = The sum of the top 30 play ratings.
- Sr = The sum of the last 10 play ratings you have.

Maximum Potential currently: 38.5

## V. What will be added in the future?
Song list has been implemented.
Song sorting has been implemented.
Song list is malleable and can be modified to update new songs (within the song_list folder).
Probably automatic difficulty setting, support for Append difficulty and JP server in the future.

## VI. Last words
The system implemented here is studied (and slightly modified) from Arcaea's Play Rating and Potential system, which you can find information about through wikis. Stuff that I have implemented here are all public information. So feel free to use it.