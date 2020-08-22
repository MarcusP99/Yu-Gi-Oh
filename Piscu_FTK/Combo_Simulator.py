import random
from combinations import *


def shuffle(deck):
    random.shuffle(deck)


def draw(deck, n):
    hand = []
    test_deck = deck.copy()
    shuffle(test_deck)
    for i in range(n):
        hand.append(test_deck.pop(0))
    return hand, test_deck


def combo(deck, n):
    success_no_hts = 0
    success_2hts = 0
    success_vs_nibiru = 0
    opened_ht = 0
    for i in range(0, n):
        test_hand, test_deck = draw(deck, 5)
        results = ftk(test_hand, test_deck)
        if results[0]:
            success_no_hts += 1
        if results[1]:
            success_2hts += 1

        if results[2]:
            success_vs_nibiru += 1

        if results[3]:
            opened_ht += 1

    no_hts_ratio = round(success_no_hts / n * 100, 2)
    two_hts_ratio = round(success_2hts / n * 100, 2)
    nibiru_ratio = round(success_vs_nibiru / n * 100, 2)
    open_ht_ratio = round(opened_ht / n * 100, 2)
    print("FTK Success Rate through no Handtraps: " + str(no_hts_ratio) + "%")
    print("FTK Success Rate through Nibiru: " + str(nibiru_ratio) + "%")
    print("FTK with atleast 1 Handtrap: " + str(open_ht_ratio) + "%")
    #print("FTK wit atleast 2 Handtraps: " + str(two_hts_ratio) + "%")

