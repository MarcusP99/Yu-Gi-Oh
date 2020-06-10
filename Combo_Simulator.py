import random
from combinations import *


def importdeck(filename):
    with open(filename) as f:
        deck = [line.strip() for line in f]
        return deck


FTK = importdeck("FTK.txt")


def shuffle(deck):
    random.shuffle(deck)


def draw(amount, deck):
    hand = []
    test_deck = deck.copy()
    shuffle(test_deck)
    for i in range(amount):
        hand.append(test_deck[0])
        test_deck.remove(test_deck[0])
    return hand


def combo(deck, n):
    success = 0
    for i in range(0, n):
        test_hand = draw(5, FTK)
        if no_hts(test_hand):
            success += 1
    ratio = round(success/n * 100, 2)
    print("FTK Probability: " + str(ratio) + "%")


simulations = 50000
combo(FTK, simulations)
