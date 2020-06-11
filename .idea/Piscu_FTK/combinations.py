# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay",
             "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring", "Infinite Impermanence"]

# List of Dragons that are cannot FTK with just itself
lv4_dragons = ["Dragon Buster Destruction Sword", "Omni Dragon Brotaur", "Red Rose Dragon", "Rokket Tracer",
               "White Rose Dragon", "Dragunity Phalanx"]

# List of cards that can be special summoned
special_summons = ["Exploderokket Dragon", "Monster Reborn", "Noctovision Dragon",
                   "Rokket Tracer", "Quick Launch", "World Legacy Guardragon", "Red-Eyes Darkness Metal Dragon",
                   "White Dragon Wyverburster", "White Rose Dragon", "Dragon Ravine"]

# List of non dragon normal summons
normal_summons = ["Effect Veiler", "Ash Blossom and Joyous Spring"]

# Deck contains 31 Monsters, so we're assuming Chaos Space and 1-4-1 are 1 Card FTKs, will adjust later
one_card_ftk = ["Black Metal Dragon", "Chaos Space", "Starliege Seyfert", "One for One"]

# List specific 2 cards that FTK that we haven't included
two_card_ftk = [["Dragon Ravine", "White Dragon Wyverburster"], ["Absorouter Dragon", "Rokket Tracer"]]

# Cards that allows us to play through handtraps (Called By, Exchange, etc), also any extenders
vs_hts = ["Called by the Grave", "Red Reboot"]


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

    win_nibiru = win & nibiru
    win_cbtg = win & cbtg
    return [win, win_cbtg, win_nibiru, open_ht]

