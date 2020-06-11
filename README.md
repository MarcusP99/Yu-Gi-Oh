# Piscu FTK Hand Simulator by Marcus Patel and Gabriel Netz

The program uses a Decklist as an input and simulates X number of 5 card hands.

Program then checks if any of the combinations of cards that can FTK are in the simulated hand.

We then return the percentage of simulated that could FTK

Decklist can be changed by adding/removing card from the FTK.txt file.


Improvements to be made:
- **Cases where the program incorrectly recognises an FTK:**
  One for One in hand and no monster to discard
  Chaos Space in hand and no valid monster to discard.
- **Post-Side Probailities**
  For Example, if we  side in Exchange this will increase the chance of playing through a handtrap going first.
- **Three-Card or more cards FTK Combos**
  There might be instances where a spefic combination of 3 or more cards that could FTK where the program might identify as a hand that could not FTK.
- **Going 2nd Hands**
  Looking at hands that can break a specific board going 2nd.
  We might want to look at hands that have a handtrap and also has a playable combo when it gets to there turn.
  **Noctovision Dragon**
  Account for Noctovision draw to play around Nib or other hts
  **Separate the 1 card ftks from Chaos Space and 1F1**
  This allows for better playing around hts
  **Train the model to do hands**
  More of a long term goal, but we could program this to set-up early hands to calculate hts more optimally. For example, if we could set up the program to play until romulous, and then opps nib, you can check if the hand plays through the said ht

**Changelist**
-Added new Two-Extender FTK Possibilities
-Removed Router and added Ravine to the "Special Summon" Array
-Fixed the Quick Launch + extender if statement to work with 2 quick launches
