from extend import *


# Verifies if hand can FTK successfully
def ftk(hand, deck):
    win = False
    play_vs_nibiru = False

    # Checks if drawn handtraps or called by the grave
    cbtg = in_hand(hand, "Called by the Grave") or in_hand(hand, "Sauravis, the Ancient and Ascended")
    open_ht, open_two_hts = two_hts(hand)


    # FTK with One card
    for i in normal_one_card_ftk:
        if i in hand:
            win = True
            temp_hand = hand.copy()
            temp_hand, deck = noctovision_draw(temp_hand, deck)
            temp_hand.remove(i)
            if "Black Metal Dragon" in hand:
                play_vs_nibiru = extend_metal(temp_hand)
            else:
                play_vs_nibiru = extend_seyfert(temp_hand)
            break

    # FTK with an extender and a dragon normal summon
    if (not win) or not play_vs_nibiru:
        for i in normal_summon_dragons:
            for j in special_summons + ["Dragunity Divine Lance"]:
                if (i in hand) & (j in hand):
                    possible_win = True

                    # Case if White Rose Dragon & Brotaur in hand, then it is not ftk
                    if ((i == j) or i == "Omni Dragon Brotaur") & (j == "White Rose Dragon"):
                        possible_win = False


                    if possible_win:
                        win = True
                        temp_hand = hand.copy()
                        temp_hand, deck = noctovision_draw(temp_hand, deck)
                        temp_hand.remove(i)
                        if (j == "Dragon Shrine") or (j == "World Legacy Guardragon"):
                            temp_hand = remove_all(temp_hand, j)
                        else:
                            temp_hand.remove(j)

                        if i == "Dragunity Phalanx":
                            play_vs_nibiru = simple_extender(temp_hand)
                        else:
                            play_vs_nibiru = extend_others(temp_hand)
                        break

    # FTK with Dragon Summonable Extender and another Extender
    if (not win) or not play_vs_nibiru:
        for i in generate_dragon_specials:
            if i in hand:
                temp_hand = hand.copy()
                if i == "Dragon Shrine":
                    temp_hand = remove_all(temp_hand, i)
                else:
                    temp_hand.remove(i)
                for j in special_summons:
                    if j in temp_hand:
                        win = True
                        temp_hand, deck = noctovision_draw(temp_hand, deck)

                        if j == "Dragon Shrine":
                            temp_hand = remove_all(temp_hand, j)
                        else:
                            temp_hand.remove(j)
                        play_vs_nibiru = extend_others(temp_hand)
                        break

    if (not win) or not play_vs_nibiru:
        if "Chaos Space" in hand:
            win = True
            temp_hand = hand.copy()
            temp_hand, deck = noctovision_draw(temp_hand, deck)
            temp_hand = remove_all(temp_hand, "Chaos Space")
            play_vs_nibiru = extend_cspace(temp_hand)

    if ((not win) or not play_vs_nibiru) & ("Absorouter Dragon" in hand):
        for i in lv4rokket_in_hand:
            if i in hand:
                win = True
                temp_hand = hand.copy()
                temp_hand.remove("Absorouter Dragon")
                temp_hand.remove(i)
                play_vs_nibiru = extend_others(temp_hand)

    if ((not win) or not play_vs_nibiru) & in_hand(hand, "Black Garden"):
        for i in tracer_in_hand:
            if i in hand:
                win = True
                temp_hand = hand.copy()
                temp_hand.remove("Black Garden")
                temp_hand.remove(i)
                play_vs_nibiru = extend_others(temp_hand)

    if ((not win) or not play_vs_nibiru) & (any(i in special_bsector for i in hand)):
        for i in generate_dragon_specials + normal_summon_dragons + ["Noctovision Dragon"]:
            if i in hand:
                win = True
                temp_hand = hand.copy()
                temp_hand, deck = noctovision_draw(temp_hand, deck)
                play_vs_nibiru = simple_extender(temp_hand)

    if (not win) or (not play_vs_nibiru):
        if "One for One" in hand:
            win = True
            if "World Legacy Guardragon" in hand:
                play_vs_nibiru = True

    # These hands cannot play through nibiru

    # Dragon Summonable Extender + Normal Summon of anything
    if (not win) or (not play_vs_nibiru):
        for i in generate_dragon_specials:
            for j in normal_summons + ["Supreme King Dragon Darkwurm"]:
                if (i in hand) & (j in hand):
                    win = True
                    break

    # FTK with specific three cards
    if (not win) or (not play_vs_nibiru):
        if ("Boot Sector Launch" in hand) & (any(i in special_bsector for i in hand)):
            if any(i in normal_summons + ["Supreme King Dragon Darkwurm"] for i in hand):
                win = True

    win_nibiru = win & play_vs_nibiru
    open_ht = win & open_ht
    open_two_hts = win & open_two_hts
    return [win, open_two_hts, win_nibiru, open_ht]
