# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay"]

# List of Dragons that are cannot FTK with just itself
lv4_dragons = ["Dragon Buster Destruction Sword", "Omni Dragon Brotaur", "Red Rose Dragon", "Rokket Tracer",
               "White Rose Dragon", "Dragunity Phalanx"]

# List of cards that can be special summoned
special_summons = ["Exploderokket Dragon", "Monster Reborn", "Noctovision Dragon",
                   "Rokket Tracer", "Quick Launch", "World Legacy Guardragon", "Red-Eyes Darkness Metal Dragon",
                   "White Dragon Wyverburster", "White Rose Dragon","Dragon Ravine"]

# List of non dragon normal summons
normal_summons = ["Effect Veiler","Ash Blossom and Joyous Spring"]



#True 1 card ftks
one_card_ftk = ["Black Metal Dragon", "Starliege Seyfert"]

#Conditional 1 card ftks
cond_one_card_ftk = ["One For One","Chaos Space"]

# List of Monsters so 1F1 and Chaos Space Discard Check
monsters = handtraps + lv4_dragons + normal_summons + special_summons
monsters.remove("Dragon Ravine")
monsters.remove("Quick Launch")
print(monsters)


# List specific 2 cards that FTK that we haven't included
two_card_ftk = [["Dragon Ravine", "White Dragon Wyverburster"],["Red Rose Dragon", "White Rose Dragon"]]

# Cards that allows us to play through handtraps (Called By, Exchange, etc), also any extenders
vs_hts = ["Called by the Grave","Red Reboot"]


# Verifies if hand can FTK successfully
def no_hts(hand):
    win = False
    cbtg = False

    if "Called by the Grave" in hand:
        cbtg = True

    # FTK with One card
    for i in range(0, len(one_card_ftk)):
        if one_card_ftk[i] in hand:
            win = True
            break

    # FTK with Conditional Card
        for i in range(0, len(one_card_ftk)):
            for j in range(0,len(monsters)):
                if (cond_one_card_ftk[i] in hand) & (monsters[j] in hand):
                    win = True
                    break


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
      
    # FTK with Quick Launch and another Extender
    if (not win) & ("Quick Launch" in hand):
        hand.remove("Quick Launch") # So we dont count the same quick launch twice
        for i in range(0, len(special_summons)):
            if special_summons[i] in hand:
                win = True
                break
        special_summons.append("Quick Launch")

    # Quick Launch + Normal Summon of anything
    if (not win) & ("Quick Launch" in hand):
      for i in range(0,len(normal_summons)):
        if normal_summons[i] in hand:
          win = True
          break

    # FTK with specific two cards, currently commented out because of time-complexity
    if not win:
        for i in range(0, len(two_card_ftk)):
            if (two_card_ftk[i][0] in hand) & (two_card_ftk[i][1] in hand):
                win = True
                break

    win_cbtg = win & cbtg
    return [win, win_cbtg]


