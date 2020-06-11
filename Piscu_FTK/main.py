from Combo_Simulator import combo


def import_deck(filename):
    with open(filename) as f:
        deck = [line.strip() for line in f]
        return deck


# What decklist we want to import and how many hands we want to simulate
def main(deck_txt, n):
    print(deck_txt)
    deck = import_deck(deck_txt)
    combo(deck, n)


main("FTK.txt", 50000)
main("FTK_no_hts.txt", 50000)