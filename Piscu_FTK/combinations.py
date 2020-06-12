# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay",
             "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring", "Infinite Impermanence"]

# List of Dragons that are cannot FTK with just itself
lv4_dragons = ["Dragon Buster Destruction Sword", "Omni Dragon Brotaur", "Red Rose Dragon", "Rokket Tracer",
               "White Rose Dragon", "Dragunity Phalanx"]

# List of cards that can be special summoned
special_summons = ["Exploderokket Dragon", "Monster Reborn", "Noctovision Dragon",
                   "Rokket Tracer", "Quick Launch", "World Legacy Guardragon", "Red-Eyes Darkness Metal Dragon",
                   "White Dragon Wyverburster", "White Rose Dragon","Dragon Ravine", "Dragon Shrine", "Foolish Burial"]

# List of non dragon normal summons
normal_summons = ["Effect Veiler", "Ash Blossom and Joyous Spring"]

generate_dragon_specials = ["Quick Launch","Dragon Shrine","Foolish Burial","Dragon Ravine"]

#True 1 card ftks
one_card_ftk = ["Black Metal Dragon", "Starliege Seyfert","Chaos Space","One for One"]

#Conditional 1 card ftks
cond_one_card_ftk = ["One For One","Chaos Space"]

# List specific 2 cards that FTK that we haven't included
two_card_ftk = [["Dragon Ravine", "White Dragon Wyverburster"],["Absorouter Dragon", "Rokket Tracer"],["Dragon Shrine","Effect Veiler"],["Foolish Burial","Effect Veiler"]]
three_card_ftk = [["Boot Sector Launch","Exploderokket Dragon","Effect Veiler"],["Boot Sector Launch","Rokket Tracer","Effect Veiler"]]

# Cards that allows us to play through handtraps (Called By, Exchange, etc), also any extenders
vs_hts = ["Called by the Grave","Red Reboot"]


# If we already have FTK, we check if we can extend with any unused cards
def extending(hand):
    return "World Legacy Guardragon" in hand


# Verifies if hand can FTK successfully
def simulations(hand):
    win = False
    cbtg = False
    nibiru = False
    open_ht = False

    if "Called by the Grave" in hand:
        cbtg = True

    # Checks if any handtraps in starting hand
    if any(i in handtraps for i in hand):
        open_ht = True

    # FTK with One card
    if any(i in one_card_ftk for i in hand):
        win = True
        nibiru = extending(hand)

    '''if 'One For One' in hand or 'Chaos Space' in hand:
        for j in range(0,len(monsters)):
            if ("One For One" in hand or "Chaos Space" in hand) & (monsters[j] in hand):
                win = True
                break'''

    # FTK with an extender and a dragon normal summon
    if not win:
        for i in range(0, len(lv4_dragons)):
            for j in range(0, len(special_summons)):
                if (lv4_dragons[i] in hand) & (special_summons[j] in hand):
                    win = True
                    # Case where both cards are rokket tracer or white rose dragon
                    if (lv4_dragons[i] == (special_summons[j])) & (i == j):
                        win = False
                    # Case if White Rose Dragon & Brotaur in hand, then it is not ftk
                    if (lv4_dragons[i] == "Omni Dragon Brotaur") & (special_summons[j] == "White Rose Dragon"):
                        win = False

                    if special_summons[j] != "World Legacy Guardragon":
                        nibiru = extending(hand)

                    if win:
                        break

    # FTK with Dragon Summonable Extender and another Extender
    if not win:
        for i in generate_dragon_specials:
            if i in hand:
                temp_hand = hand
                temp_hand.remove(i)
                for j in range(len(special_summons)):
                    if special_summons[j] in temp_hand:
                        win = True
                        if special_summons[j] != "World Legacy Guardragon":
                            nibiru = extending(hand)
                        break

    # FTK with Quick Launch and another Extender
    if (not win) & ("Quick Launch" in hand):
        hand.remove("Quick Launch")  # So we dont count the same quick launch twice
        for i in range(0, len(special_summons)):
            if special_summons[i] in hand:
                win = True
                nibiru = extending(hand)
                break
        hand.append("Quick Launch")

    # Quick Launch + Normal Summon of anything
    if (not win) & ("Quick Launch" in hand):
        for i in range(0, len(normal_summons)):
            if normal_summons[i] in hand:
                win = True
                nibiru = extending(hand)
                break

    # FTK with specific two cards
    if not win:
        for i in range(0, len(two_card_ftk)):
            if (two_card_ftk[i][0] in hand) & (two_card_ftk[i][1] in hand):
                win = True
                nibiru = extending(hand)
                break

    if not win:
        for i in range(0, len(three_card_ftk)):
            if (three_card_ftk[i][0] in hand) & (three_card_ftk[i][1] in hand) & (three_card_ftk[i][2] in hand):
                win = True
                break

    win_nibiru = win & nibiru
    win_cbtg = win & cbtg
    return [win, win_cbtg, win_nibiru, open_ht]


def checklists(list,hand):
    for i in list:
        for j in hand:
            if i == j:
                return True
    return False