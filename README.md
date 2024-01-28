# The Project Sekai Performance Tracker
## I. What is this?
It's a program that tracks your pjsk performance using Arcaea's Potential and Scoring System.

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
- For scores above 10000000 : 2.0
- For scores above  9800000 : score_modifier = 1.0 + (score - 9800000) / 200000
- Other                     : score_modifier = (score - 9500000) / 300000
Then the score modifier is added to the difficulty to get the play rating, which is used for the Potential system.

## IV. Potential calculation
Internally, scores are saved in 2 different files:
- Global play, which keep track of every score you have.
- Recent play, which keep track of the last 10 scores you got.
To calculate the potential, the top 30 score (dictated by play ratings) are taken into account alongside the last 10 scores you got.
The calculation is: (Sg + Sr) / 40
With:
- Sg = The sum of the top 30 play ratings.
- Sr = The sum of the last 10 play ratings you have.

## V. What will be added in the future?
Right now the input field is rather fragile, as it doesn't automatically filter out special characters. In the future, a system would be added in place to prevent the same song from appearing twice. Probably by implementing the whole song list, maybe maybe.

## VI. Last words
The system implemented here is studied from Arcaea's Play Rating and Potential system, which you can find information about through wikis. Stuff that I have implemented here are all public information. So feel free to use it.