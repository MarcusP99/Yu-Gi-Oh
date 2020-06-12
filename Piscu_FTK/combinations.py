from sets import *


# Verifies if hand can FTK successfully
def simulations(hand):
    win = False
    nibiru = False

    # Checks if drawn handtraps or called by the grave
    cbtg = called_by(hand)
    open_ht = hts(hand)

    # FTK with One card
    for i in one_card_ftk:
        if i in hand:
            hand.remove(i)
            nibiru = extending(hand)
            win = True
            break

    '''if 'One For One' in hand or 'Chaos Space' in hand:
        for j in range(0,len(monsters)):
            if ("One For One" in hand or "Chaos Space" in hand) & (monsters[j] in hand):
                win = True
                break'''

    # FTK with an extender and a dragon normal summon
    if not win:
        for i in lv4_dragons:
            for j in special_summons:
                if (i in hand) & (j in hand):
                    win = True

                    # Case where both cards are rokket tracer or white rose dragon
                    if i == j:
                        win = False
                    # Case if White Rose Dragon & Brotaur in hand, then it is not ftk
                    if (i == "Omni Dragon Brotaur") & (j == "White Rose Dragon"):
                        win = False

                    if win:
                        hand.remove(i)
                        hand.remove(j)
                        if j != "World Legacy Guardragon":
                            nibiru = extending(hand)
                        break

    # FTK with Dragon Summonable Extender and another Extender
    if not win:
        for i in generate_dragon_specials:
            if i in hand:
                temp_hand = hand.copy()
                temp_hand.remove(i)
                for j in special_summons:
                    if j in temp_hand:
                        win = True
                        if j != "World Legacy Guardragon":
                            nibiru = extending(hand)
                        break

    # FTK with Quick Launch and another Extender
    if (not win) & ("Quick Launch" in hand):
        hand.remove("Quick Launch")  # So we don't count the same quick launch twice
        for i in special_summons:
            if i in hand:
                win = True
                nibiru = extending(hand)
                break
        hand.append("Quick Launch")

    # Quick Launch + Normal Summon of anything
    if (not win) & ("Quick Launch" in hand):
        for i in normal_summons:
            if i in hand:
                win = True
                nibiru = extending(hand)
                break

    # FTK with specific two cards
    if not win:
        for i in two_card_ftk:
            if (i[0] in hand) & (i[1] in hand):
                win = True
                nibiru = extending(hand)
                break

    # FTK with specific three cards
    if not win:
        for i in three_card_ftk:
            if (i[0] in hand) & (i[1] in hand) & (i[2] in hand):
                win = True
                nibiru = extending(hand)
                break

    win_nibiru = win & nibiru
    win_cbtg = win & (cbtg or nibiru)
    return [win, win_cbtg, win_nibiru, open_ht]
