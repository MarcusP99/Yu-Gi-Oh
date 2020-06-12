# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay",
             "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring", "Infinite Impermanence"]

# List of Dragons that are cannot FTK with just itself
normal_summon_dragons = ["Dragon Buster Destruction Sword", "Omni Dragon Brotaur", "Red Rose Dragon", "Rokket Tracer",
               "White Rose Dragon", "Dragunity Phalanx"]

# List of cards that can be special summoned
special_summons = ["Exploderokket Dragon", "Monster Reborn", "Noctovision Dragon",
                   "Rokket Tracer", "Quick Launch", "World Legacy Guardragon", "Red-Eyes Darkness Metal Dragon",
                   "White Dragon Wyverburster", "White Rose Dragon", "Dragon Ravine", "Dragon Shrine", "Foolish Burial"]

# List of non dragon normal summons
normal_summons = ["Effect Veiler", "Ash Blossom and Joyous Spring"]

generate_dragon_specials = ["Quick Launch", "Dragon Shrine", "Foolish Burial", "Dragon Ravine"]

# True 1 card ftks
one_card_ftk = ["Black Metal Dragon", "Starliege Seyfert", "Chaos Space", "One for One"]

# Conditional 1 card ftks
cond_one_card_ftk = ["One For One", "Chaos Space"]

# List specific 2 cards that FTK that we haven't included
two_card_ftk = [["Dragon Ravine", "White Dragon Wyverburster"], ["Absorouter Dragon", "Rokket Tracer"],
                ["Dragon Shrine", "Effect Veiler"], ["Foolish Burial", "Effect Veiler"]]
three_card_ftk = [["Boot Sector Launch", "Exploderokket Dragon", "Effect Veiler"],
                  ["Boot Sector Launch", "Rokket Tracer", "Effect Veiler"]]

# Cards that allows us to play through handtraps (Called By, Exchange, etc), also any extenders
vs_hts = ["Called by the Grave", "Red Reboot"]

# One card cards that play through Nibiru
vs_nibiru = ["World Legacy Guardragon", "One for One"]

# List of Lv4 lv4_dragon
actual_lv4_dragons = ["White Dragon Wyverburster","Rokket Tracer","Starliege Seyfert","Black Dragon Collapserpent", "White Rose Dragon","Supreme King Dragon Darkwurm" ]

tracer_in_hand = generate_dragon_specials + ["Rokket Tracer"]

with_abso = ["White Dragon Wyverburster", "Quick Launch","Black Dragon Collapserpent", "Monster Reborn"]

once_per_turn = ["Dragon Shrine", "World Legacy Guardragon", "Chaos Space", "Noctovision Dragon"]


# If we already have FTK, we check if we can extend with any unused cards
def extending(hand, seyfert):
    extend = False

    if any(i in vs_nibiru for i in hand):
        extend = True

    if "Quick Launch" in hand:
        hand.remove("Quick Launch")
        if "Quick Launch" in hand:
            extend = True

    if seyfert & any(i in tracer_in_hand for i in hand) & any(i in actual_lv4_dragons for i in hand):
        extend = True

    if seyfert & ("Absorouter Dragon" in hand) & any(i in with_abso for i in hand):
        extend = True

    return extend


# Checks if we have drawn called by the grave
def in_hand(hand, card):
    return card in hand


def hts(hand):
    return any(i in handtraps for i in hand)


# Remove cards in hands if they FTK
def checklists(list, hand):
    for i in list:
        for j in hand:
            if i == j:
                return True
    return False
