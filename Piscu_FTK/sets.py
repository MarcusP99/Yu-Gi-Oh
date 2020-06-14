# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay",
             "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring", "Infinite Impermanence"]

# List of Dragons that are cannot FTK with just itself
normal_summon_dragons = ["Dragon Buster Destruction Sword", "Omni Dragon Brotaur", "Red Rose Dragon",
                         "Dragunity Phalanx", "Supreme King Dragon Darkwurm", "White Rose Dragon", "Rokket Tracer"]

# List of cards that can be special summoned
special_summons = ["Noctovision Dragon", "Monster Reborn", "Quick Launch", "World Legacy Guardragon",
                   "Red-Eyes Darkness Metal Dragon", "White Dragon Wyverburster", "White Rose Dragon", "Dragon Ravine",
                   "Dragon Shrine", "Foolish Burial"]

special_bsector = ["Exploderokket Dragon", "Rokket Tracer"]

# List of non dragon normal summons
normal_summons = ["Effect Veiler", "Ash Blossom & Joyous Springs"]

generate_dragon_specials = ["Quick Launch", "Dragon Shrine", "Foolish Burial", "Dragon Ravine"]

# True 1 card ftks
one_card_ftk = ["Black Metal Dragon", "Starliege Seyfert"]

# Conditional 1 card ftks
cond_one_card_ftk = ["One for One", "Chaos Space"]

# List specific 2 cards that FTK that we haven't included
two_card_ftk = [["Dragon Ravine", "White Dragon Wyverburster"],
                ["Dragon Shrine", "Effect Veiler"], ["Foolish Burial", "Effect Veiler"]]
three_card_ftk = [["Boot Sector Launch", "Exploderokket Dragon", "Effect Veiler"],
                  ["Boot Sector Launch", "Rokket Tracer", "Effect Veiler"]]

# Cards that allows us to play through handtraps (Called By, Exchange, etc), also any extenders
vs_hts = ["Called by the Grave", "Red Reboot"]

# One card cards that play through Nibiru
vs_nibiru = ["World Legacy Guardragon", "One for One"]

# List of Lv4 lv4_dragon
actual_lv4_dragons = ["White Dragon Wyverburster", "Rokket Tracer", "Starliege Seyfert", "Black Dragon Collapserpent",
                      "White Rose Dragon", "Supreme King Dragon Darkwurm", "Chaos Space"]

tracer_in_hand = generate_dragon_specials + ["Rokket Tracer"]

lv4_dragon_extenders = ["White Dragon Wyverburster", "Quick Launch", "Black Dragon Collapserpent", "Monster Reborn",
                        "Chaos Space", "White Rose Dragon"]

mini_chaos = ["White Dragon Wyverburster", "Chaos Space", "Black Dragon Collapserpent"]

once_per_turn = [["Dragon Shrine", False], ["World Legacy Guardragon", False],
                 ["Noctovision Dragon", False]]

dragon_extenders = ["Quick Launch", "Monster Reborn", "White Rose Dragon"]


def noctodraw(hand, deck):
    top_card = deck[0]
    hand.append(top_card)
    return hand, deck
