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
    return hand


def combo(deck, n):
    success_no_hts = 0
    success_1cbtg = 0
    success_vs_nibiru = 0
    opened_ht = 0
    for i in range(0, n):
        test_hand = draw(deck, 5)
        shuffle(deck)
        results = ftk(test_hand, deck)
        if results[0]:
            success_no_hts += 1

        if results[1]:
            success_1cbtg += 1

        if results[2]:
            success_vs_nibiru += 1

        if results[3]:
            opened_ht += 1

    no_hts_ratio = round(success_no_hts / n * 100, 2)
    one_cbtg_ratio = round(success_1cbtg / n * 100, 2)
    nibiru_ratio = round(success_vs_nibiru / n * 100, 2)
    open_ht_ratio = round(opened_ht / n * 100, 2)

    print("FTK Success Rate through no Handtraps: " + str(no_hts_ratio) + "%")
    print("FTK Success Rate through 1 discardable Handtrap: " + str(one_cbtg_ratio) + "%")
    print("FTK Success Rate through Nibiru: " + str(nibiru_ratio) + "%")
    print("Hands with atleast 1 handtrap: " + str(open_ht_ratio) + "%\n")


def go_second(deck,n):
    # Placeholder for now
    return True