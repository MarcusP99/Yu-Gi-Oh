# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay"]

# List of Dragons that are cannot FTK with just itself
lv4_dragons = ["Dragon Buster Destruction Sword", "Omni Dragon Brotaur", "Red Rose Dragon", "Rokket Tracer",
               "White Rose Dragon", "Dragunity Phalanx", "Supreme King Darkwurm"]

# List of cards that can be special summoned
special_summons = ["Exploderokket Dragon", "Monster Reborn", "Noctovision Dragon",
                   "Rokket Tracer", "Quick Launch", "World Legacy Guardragon", "Red-Eyes Darkness Metal Dragon",
                   "White Dragon Wyverburster", "White Rose Dragon","Dragon Ravine", "Dragon Shrine", "Foolish Burial"]

# List of non dragon normal summons
normal_summons = ["Effect Veiler","Ash Blossom and Joyous Spring"]

generate_dragon_specials = ["Quick Launch","Dragon Shrine","Foolish Burial","Dragon Ravine"]

#True 1 card ftks
one_card_ftk = ["Black Metal Dragon", "Starliege Seyfert","Chaos Space","One for One"]

#Conditional 1 card ftks
cond_one_card_ftk = ["One For One","Chaos Space"]

# List of Monsters so 1F1 and Chaos Space Discard Check
monsters = handtraps + lv4_dragons + normal_summons + special_summons
monsters.remove("Dragon Ravine")
monsters.remove("Quick Launch")
monsters.append("Chaos Dragon Levianner")
print(monsters)


# List specific 2 cards that FTK that we haven't included
two_card_ftk = [["Dragon Ravine", "White Dragon Wyverburster"],["Red Rose Dragon", "White Rose Dragon"],["Dragon Shrine","Effect Veiler"],["Foolish Burial","Effect Veiler"]]
three_card_ftk = [["Boot Sector Launch","Exploderokket Dragon","Effect Veiler"],["Boot Sector Launch","Rokket Tracer","Effect Veiler"]]

# Cards that allows us to play through handtraps (Called By, Exchange, etc), also any extenders
vs_hts = ["Called by the Grave","Red Reboot"]


# Verifies if hand can FTK successfully
def no_hts(hand):
    win = False
    cbtg = False

    # FTK with One card
    for i in range(0, len(one_card_ftk)):
        if one_card_ftk[i] in hand:
            win = True
            break


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
                    if (lv4_dragons[i] == "Omni Dragon Brotaur" ) & (special_summons[j] == "White Rose Dragon"):
                        win = False

                    if win:
                        break

    # FTK Tracer + Router
    if (not win) & ("Absorouter Dragon" in hand) & ("Rokket Tracer" in hand):
      win = True

    # FTK with Dragon Summonable Extender and another Extender
    if not win:
        for i in generate_dragon_specials:
            if i in hand:
                temp_hand = hand
                temp_hand.remove(i)
                for j in range(len(special_summons)):
                    if special_summons[j] in temp_hand:
                        win = True
                        break


    # Quick Launch + Normal Summon of anything
    if (not win) & (("Quick Launch" in hand) or ("Dragon Shrine" in hand) or ("Foolish Burial" in hand)):
      for i in range(len(normal_summons)):
        if normal_summons[i] in hand:
          win = True
          break

    # FTK with specific two cards, currently commented out because of time-complexity
    if not win:
        for i in range(0, len(two_card_ftk)):
            if (two_card_ftk[i][0] in hand) & (two_card_ftk[i][1] in hand):
                win = True
                break

    if not win:
        for i in range(0, len(three_card_ftk)):
            if (three_card_ftk[i][0] in hand) & (three_card_ftk[i][1] in hand) & (three_card_ftk[i][2] in hand):
                win = True
                break

    if win is True:
        pass
    else:
        print(hand)
        print("not ftk")
    if "Called by the Grave" in hand:
        cbtg = True
    win_cbtg = win & cbtg
    return [win, win_cbtg]



def checklists(list,hand):
    for i in list:
        for j in hand:
            if i == j:
                return True
    return False
