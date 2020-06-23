# Piscu FTK Hand Simulator by Marcus Patel

The program uses a Decklist as an input and simulates X number of 5 card hands.

Program then checks if any of the combinations of cards that can FTK are in the simulated hand.

We then return the percentage of the simulated hands that successfully FTK'ed

Decklist can be changed by adding/removing card from the FTK.txt file.

Results:
It won the tournament, first deck to do so, major congratulations to Tristan Pugh who piloted the deck to 1st Place, 
he went unbeaten throughout swiss and the knockout stages which is rare in a game that includes variance.

A very big accomplishment to create a deck from scratch in a meta-game where everyone believed everything was solved.

It broke the format.


Covered by major figures in the community:
https://www.youtube.com/watch?v=IwafVNwseWc&t=110s
https://www.youtube.com/watch?v=6BX-eRxLx6o
 


Got a shoutout from Tristan in most of these videos.


Improvements to be made:
- **Cases where the program incorrectly recognises an FTK:**
  One for One in hand and no monster to discard
  Chaos Space in hand and no valid monster to discard.
- **Post-Side Probailities**
  For Example, if we  side in Exchange this will increase the chance of playing through a handtrap going first.
- **Going 2nd Hands**
  Looking at hands that can break a specific board going 2nd.
  We might want to look at hands that have a handtrap and also has a playable combo when it gets to there turn.
  **Chaos Space Draw**
  Account for Chaos Space draw to play around Nib or other hts


**Changelist**
- Added Noctovision function
- Able to remove all OPT cards when used
- Completed majority of the Nibiru cases