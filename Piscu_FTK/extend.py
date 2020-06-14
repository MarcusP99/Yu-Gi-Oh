from sets import *


# # If we already have FTK, we check if we can extend with any unused cards
# def extending(hand, seyfert):
#     extend = False
#
#     if "Quick Launch" in hand:
#         hand.remove("Quick Launch")
#         if "Quick Launch" in hand:
#             extend = True
#
#     if seyfert & any(i in tracer_in_hand for i in hand) & any(i in lv4_dragons for i in hand):
#         extend = True
#
#     if seyfert & ("Absorouter Dragon" in hand) & any(i in lv4_dragon_extenders for i in hand):
#         extend = True
#
#     if ("Dragon Ravine" in hand or "Dragunity Divine Lance" in hand) & any(i in dragon_extenders for i in hand):
#         extend = True
#
#     return extend

def midcombo_tracer(hand):
    return any(i in tracer_in_hand + ["Dragunity Divine Lance"] for i in hand)


def simple_extender(hand):
    return any(i in vs_nibiru for i in hand)


def tracer_with_extender(hand):
    extend = False
    tracer = midcombo_tracer(hand)
    if not tracer:
        return False
    if ("Absorouter Dragon" in hand) or any(i in mini_chaos for i in hand) or any(
            i in lv4_dragon_extenders for i in hand):
        extend = True
    return extend


def extend_others(hand):
    return simple_extender(hand) or tracer_with_extender(hand)


def extend_metal(hand):
    extend = simple_extender(hand)
    if extend:
        return extend
    else:
        extend = tracer_with_extender(hand)

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
        extend = tracer_with_extender(hand)

    if extend:
        return extend
    else:
        extend = midcombo_tracer(hand) & any(i in lv4_dragons for i in hand)
    return extend


def extend_cspace(hand):
    extend = simple_extender(hand)
    if extend:
        return extend

    if midcombo_tracer(hand):
        extend = ("Absorouter Dragon" in hand) or any(i in lv4_dragon_extenders for i in hand)

    if (not extend) & (midcombo_tracer(hand) or "Monster Reborn" in hand) & any(i in normal_summons for i in hand):
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
