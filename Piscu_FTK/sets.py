# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay",
             "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring", "Infinite Impermanence"]

# List of Dragons that are cannot FTK with just itself
normal_summon_dragons = ["Dragon Buster Destruction Sword", "Omni Dragon Brotaur", "Red Rose Dragon",
                         "Dragunity Phalanx", "White Rose Dragon", "Rokket Tracer"]

# List of cards that can be special summoned
special_summons = ["Noctovision Dragon", "Monster Reborn", "Quick Launch",
                   "Red-Eyes Darkness Metal Dragon", "White Dragon Wyverburster", "White Rose Dragon", "Dragon Ravine",
                   "Dragon Shrine", "Foolish Burial", "World Legacy Guardragon"]

special_bsector = ["Exploderokket Dragon", "Rokket Tracer"]

# List of non dragon normal summons
normal_summons = ["Effect Veiler", "Ash Blossom & Joyous Springs"]

generate_dragon_specials = ["Quick Launch", "Dragon Shrine", "Foolish Burial", "Dragon Ravine"]

normal_one_card_ftk = ["Black Metal Dragon", "Starliege Seyfert"]

# One card cards that play through Nibiru
vs_nibiru = ["World Legacy Guardragon", "One for One"]

# List of Lv4 lv4_dragon
lv4_dragons = ["White Dragon Wyverburster", "Rokket Tracer", "Starliege Seyfert", "Black Dragon Collapserpent",
               "White Rose Dragon", "Supreme King Dragon Darkwurm", "Chaos Space"]

tracer_in_hand = generate_dragon_specials + ["Rokket Tracer"]

lv4_dragon_extenders = ["Quick Launch", "Monster Reborn", "White Rose Dragon"]

mini_chaos = ["White Dragon Wyverburster", "Chaos Space", "Black Dragon Collapserpent"]


def noctovision_draw(hand, deck):
    if "Noctovision Dragon" in hand:
        top_card = deck[0]
        hand.append(top_card)
    return hand, deck


def remove_all(hand, used):
    return [card for card in hand if card != used]
