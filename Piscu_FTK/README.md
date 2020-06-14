# Piscu FTK Hand Simulator by Marcus Patel

The program uses a Decklist as an input and simulates X number of 5 card hands.

Program then checks if any of the combinations of cards that can FTK are in the simulated hand.

We then return the percentage of the simulated hands that successfully FTK'ed

Decklist can be changed by adding/removing card from the FTK.txt file.


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
  **Separate the 1 card ftks from Chaos Space and 1F1**
  This allows for better playing around hts
  **Train the model to do hands**
  More of a long term goal, but we could program this to set-up early hands to calculate hts more optimally. For example, if we could set up the program to play until romulous, and then opps nib, you can check if the hand plays through the said ht
  **Handtraps**
  Adjust the Handtrap percentage by excluding phantazmay and including the chance to draw nibiru/veiler(disruptions mid-combo) from phantazmay. Maybe include average number of handtraps drawn in the output

**Changelist**
- Added Noctovision function
- Able to remove all OPT cards when used
- Completed majority of the Nibiru cases
