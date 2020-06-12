# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay",
             "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring", "Infinite Impermanence"]

# List of Dragons that are cannot FTK with just itself
lv4_dragons = ["Dragon Buster Destruction Sword", "Omni Dragon Brotaur", "Red Rose Dragon", "Rokket Tracer",
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


# If we already have FTK, we check if we can extend with any unused cards
def extending(hand):
    return any(i in vs_nibiru for i in hand)


# Checks if we have drawn called by the grave
def called_by(hand):
    return "Called by the Grave" in hand


def hts(hand):
    return any(i in handtraps for i in hand)

# Remove cards in hands if they FTK
def checklists(list, hand):
    for i in list:
        for j in hand:
            if i == j:
                return True
    return False
