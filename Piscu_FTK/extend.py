from sets import *


#Rewrite Midcombo + Tracer
def midcombo_tracer(hand):
    tracer = False
    for i in tracer_in_hand:
        if i in hand:
            tracer = True
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
            extend = any(i in lv4_dragons + lv4_dragon_extenders + tracer_in_hand + ["Dragunity Divine Lance"] for i in hand)
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
        hand, tracer = midcombo_tracer(hand)
        extend = tracer & any(i in lv4_dragons for i in hand)
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
    return extend


# Checks if we have drawn called by the grave
def in_hand(hand, card):
    return card in hand


def hts(hand):
    return any(i in handtraps for i in hand)

# def used_opt(hand, card):
#     used = False
#     for i in once_per_turn:
#         if card in i[0]:
#             if i[1]:
#                 used = True
#             else:
#                 i[1] = True
#     return used
#
#
# def reset_opt(opt):
#     return [["Dragon Shrine", False], ["World Legacy Guardragon", False], ["Noctovision Dragon", False]]

#
# # Remove cards in hands if they FTK
# def checklists(list, hand):
#     for i in list:
#         for j in hand:
#             if i == j:
#                 return True
#     return False
