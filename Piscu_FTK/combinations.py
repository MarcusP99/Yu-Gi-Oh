from extend import *


# Verifies if hand can FTK successfully
def ftk(hand, deck):
    win = False
    nibiru = False
    seyfert = in_hand(hand, "Starliege Seyfert")
    black_garden = in_hand(hand, "Black Garden")
    unused_boot_sector = False

    # Checks if drawn handtraps or called by the grave
    cbtg = in_hand(hand, "Called by the Grave") or in_hand(hand, "Sauravis, the Ancient and Ascended")
    open_ht = hts(hand)

    # FTK with One card
    for i in (one_card_ftk + cond_one_card_ftk):
        if i in hand:
            hand.remove(i)
            nibiru = extending(hand, seyfert)
            win = True
            break


    # FTK with an extender and a dragon normal summon
    if not win:
        for i in normal_summon_dragons:
            for j in special_summons:
                if (i in hand) & (j in hand):
                    win = True

                    # Case where both cards froms sets are not rokket tracer
                    if (i == j) & (i != "Rokket Tracer"):
                        win = False
                    # Case if White Rose Dragon & Brotaur in hand, then it is not ftk
                    if (i == "Omni Dragon Brotaur") & (j == "White Rose Dragon"):
                        win = False

                    if win:
                        hand.remove(i)
                        if i != j:
                            hand.remove(j)
                        # if j == "Noctovision Dragon":
                        #     hand = hand.append(deck.pop(0))
                        if j != "World Legacy Guardragon":
                            nibiru = extending(hand, seyfert)
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
                        hand.remove(i)
                        hand.remove(j)
                        if j == "Noctovision Dragon":
                            hand, deck = noctodraw(hand, deck)
                        if j != "World Legacy Guardragon":
                            nibiru = extending(hand, seyfert)
                        break

    # Dragon Summonable Extender + Normal Summon of anything
    if not win:
        for i in generate_dragon_specials:
            for j in normal_summons:
                if (i in hand) & (j in hand):
                    win = True
                    hand.remove(i)
                    hand.remove(j)
                    nibiru = extending(hand, seyfert)
                    break

    # FTK with specific two cards
    if not win:
        for i in two_card_ftk:
            if (i[0] in hand) & (i[1] in hand):
                win = True
                hand.remove(i[0])
                hand.remove(i[1])
                nibiru = extending(hand, seyfert)
                break

    # FTK with specific three cards
    if not win:
        for i in three_card_ftk:
            if (i[0] in hand) & (i[1] in hand) & (i[2] in hand):
                win = True
                hand.remove(i[0])
                hand.remove(i[1])
                hand.remove(i[2])
                nibiru = extending(hand, seyfert)
                break

    if not win:
        if ("Absorouter Dragon" in hand) & any(i in tracer_in_hand for i in hand):
            win = True

    if (not win) & black_garden:
        if any(i in tracer_in_hand for i in hand):
            win = True

    win_nibiru = win & nibiru
    win_cbtg = win & (cbtg or nibiru)
    return [win, win_cbtg, win_nibiru, open_ht]
