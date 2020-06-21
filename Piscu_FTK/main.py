from Combo_Simulator import combo


def import_deck(filename):
    with open(filename) as f:
        deck = [line.strip() for line in f if not line.startswith('#')]
        return deck


# What decklist we want to import and how many hands we want to simulate
def main(deck_txt, n):
    print(deck_txt)
    deck = import_deck(deck_txt)
    combo(deck, n)


# main("FTK.txt", 50000)
# main("FTK_no_hts.txt", 50000)
# main("FTK_56.txt", 50000)
# main("FTK_58.txt", 50000)
#main("FTK_60_w_3Nocto.txt", 200000)
print("Rokket Synchron in Deck")
# main("FTK_60_w_3cbtg.txt", 100000)
# main("FTK_57_no_cbtg.txt", 100000)
main("FTK_60_no_cbtg.txt", 100000)


