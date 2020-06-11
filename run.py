from Combo_Simulator import combo

def import_deck(filename):
    with open(filename) as f:
        deck = [line.strip() for line in f]
        return deck


# What decklist we want to import and how many hands we want to simulate
#FTK = import_deck("FTK.txt")
FTK = import_deck("FTKnoHT.txt")
combo(FTK, 10000)
