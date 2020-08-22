# YUGIOH Piscu FTK Hand Probability Simulator by Marcus Patel

## Background

A teammate (Gabriel Netz) figured how using a certain combination of cards would allow a player to win the first turn of a game of Yu-Gi-Oh.
This was rare as strategies like these are usually recognised and then banned by the game organisers (Konami), 
so we saw an opportunity to take advantage of this and shape the current meta game.

In the card game Yu-Gi-Oh!, players create decks of cards between 40 to 60, all cards have unique interactions.
We had 2 weeks to optimise a deck based around the strategy to win the first turn, this is a short time frame as most meta 
decks takes months and hundreds of tournaments worldwide to reach a solved state.
There are many variables to consider when building a Yu-Gi-Oh deck, however the strategy of this deck was to win in the first turn.

By being able to calculate this value we could compare decklists, this would be difficult without programming as the 
current standard to work out the consistency of a deck is to draw the cards out in real life.

We figured out the way to play this deck was to play maximises the amount of cards in a Yu-Gi-Oh deck (60). This is very
controversial as nearly all competitive decks are built to play the minimum amount of cards (40) as possible in order to draw
the most valuable cards.

## Successes
This deck was made in preparation for a major online event (20/07/2020 - LCS4) won event, it had a shocking impact on the community.
The person who piloted this deck was undefeated after 8 rounds and then the knockout stages this is very uncommon 
in card games as there is an aspect of variance so a massive congratulations to Tristan Pugh.

I made a Youtube video going through this project as this was a new concept of using programming as a tool to construct Yu-Gi-Oh! decks. 
Which can be found here: https://www.youtube.com/watch?v=fNiyaKrNPF8&t=122s \
This was video received highly positive feedback from the community, as no one had shared content like this.

Many major figures in the community made videos about this deck where the links can be found here:\
https://www.youtube.com/watch?v=6BX-eRxLx6o \
https://www.youtube.com/watch?v=IwafVNwseWc&t \
https://www.youtube.com/watch?v=iHEtQvnvHOo&t (He linked my math video in the description) \
https://www.reddit.com/r/yugioh/comments/hf405q/how_you_can_use_programming_to_optimise_your/
 
 
## How it works
The program uses a "Decklist" as an input and simulates X number of 5 card hands. \
Decklist can be edited by adding/removing cards from the txt files however, this will only have an impact on the results if the card is featured in the code. \
The program then checks if any of the combinations of cards that can FTK are in the simulated hand. \
We then return the percentage of the simulated hands that successfully FTK'ed. 

Testing was very important when developing this project, as we knew what combination of cards would lead to success, 
we would easily be able to check for errors as changes were made. This helped identify and solve errors making sure the
code was providing reliable information. 

There are also cards that our opponent can play that would interrupt the FTK, so we also calculated this value, 
it is important as we could identify cards which would allows us to play more optimally vs barriers.

##Usage
To program runs with no additional cmd line arguments (python3 main.py), to change the number of hand simulations or 
decklist used, you have to manually edit the main file.\
This was done to make it as user friendly as possible to those not familiar with coding as I had share this on repl under the Youtube link.

Test Cases can be run through python3 test_cases.py

**This program won't be improved on anymore as the event the deck was made for has been completed.**

## Contributions
Shoutouts to Tristan Pugh for winning with the deck, Gabriel Netz for creating the combo and helping with the code and 
Samuel Pearson who helped with playtesting. We all spent the two weeks prior to the event playtesting with the deck, 
figuring out all the combos through various different handtraps and alot of niche scenarios which helped made this code 
and the information provided from it possible.



