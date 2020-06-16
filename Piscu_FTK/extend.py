from sets import *


# Rewrite Midcombo + Tracer
def midcombo_tracer(hand):
    tracer = False
    for i in lv4rokket_in_hand:
        if i in hand:
            tracer = True
            if (i == "Dragon Shrine") or (i == "Rokket Tracer"):
                hand = remove_all(hand, i)
            else:
                hand.remove(i)
            break

    return hand, tracer


def simple_extender(hand):
    return any(i in vs_nibiru for i in hand)


def tracer_with_extender(hand):
    extend = False

    hand, tracer = midcombo_tracer(hand)
    if not tracer:
        return False
    if ("Absorouter Dragon" in hand) or any(i in mini_chaos for i in hand) or any(i in lv4_dragon_extenders for i in hand):
        extend = True
    if not extend:
        if any(i in ["Rokket Tracer", "Rokket Synchron"] for i in hand):
            extend = True
    return extend


def extend_others(hand):
    return simple_extender(hand) or tracer_with_extender(hand)


def extend_metal(hand):
    extend = simple_extender(hand)
    if extend:
        return extend
    else:
        extend = tracer_with_extender(hand.copy())

    if extend:
        return extend
    else:
        if "Starliege Seyfert" in hand:
            extend = any(
                i in lv4_dragons + lv4_dragon_extenders + tracer_in_hand + ["Dragunity Divine Lance"] for i in hand)
    return extend


def extend_seyfert(hand):
    extend = simple_extender(hand)

    if extend:
        return extend
    else:
        extend = tracer_with_extender(hand.copy())

    if extend:
        return extend
    else:
        temp_hand = hand.copy()
        for i in lv4_dragons:
            if i in hand:
                temp_hand.remove(i)
                temp_hand, tracer = midcombo_tracer(temp_hand)
                extend = tracer
    return extend


def extend_cspace(hand):
    extend = simple_extender(hand)
    if extend:
        return extend

    hand, tracer = midcombo_tracer(hand)
    if tracer:
        extend = ("Absorouter Dragon" in hand) or any(i in lv4_dragon_extenders for i in hand)

    if (not extend) & (tracer or "Monster Reborn" in hand) & any(i in normal_summons for i in hand):
        extend = True

    if (not extend) & tracer & any(i in ["Rokket Tracer", "Rokket Synchron"] for i in hand):
        extend = True

    return extend


# Checks if we have drawn called by the grave
def in_hand(hand, card):
    return card in hand


def hts(hand):
    return any(i in handtraps for i in hand)


def two_hts(hand):
    open_one_ht = False
    open_two_hts = False
    for i in hand:
        if i in handtraps:
            open_one_ht = True
            if i in opt_handtraps:
                open_two_hts = hts(remove_all(hand.copy(), i))
            else:
                temp_hand = hand.copy()
                temp_hand.remove(i)
                open_two_hts = hts(temp_hand)
    return open_one_ht, open_two_hts
