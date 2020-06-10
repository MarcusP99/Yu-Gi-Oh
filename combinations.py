import random

one_card_ftk = ["Black Metal Dragon", "Chaos Space", "Starliege Seyfert"]


def no_hts(hand):
    win = False
    for i in range(0, len(one_card_ftk)):
        if one_card_ftk[i] in hand:
            win = True
            break
    return win

