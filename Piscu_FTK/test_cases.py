from combinations import ftk


# One card FTKs
def one_card():
    assert ftk(["Black Metal Dragon"])[0]
    assert ftk(["Starliege Seyfert"])[0]
    return True


# Hands that ftk with two cards
def two_card():
    assert ftk(["White Rose Dragon", "Red Rose Dragon"])[0]
    assert ftk(["Omni Dragon Brotaur", "Rokket Tracer"])[0]
    assert ftk(["Quick Launch", "Quick Launch"])[0]
    assert ftk(["Quick Launch", "Monster Reborn"])[0]
    assert ftk(["Quick Launch", "Effect Veiler"])[0]
    assert not ftk(["White Rose Dragon", "Omni Dragon Brotaur"])[0]
    assert ftk(["Dragon Shrine", "Effect Veiler"])[0]

    return True


# Hands that ftk with three cards
def three_card():
    assert ftk(["Boot Sector Launch", "Exploderokket Dragon", "Effect Veiler"])[0]
    assert ftk(["Boot Sector Launch", "Rokket Tracer", "Effect Veiler"])[0]
    return True


# FTKs we have recognised give a wrong result
def incorrect_ftks():
    assert ftk(["Dragon Shrine", "Dragon Shrine"])[0]
    assert ftk(["One for One", "Spell"])[0]
    assert ftk(["Chaos Space", "Spell"])[0]
    return True


# Hands that can combo through nibiru
def vs_nibiru():
    assert ftk(["Black Metal Dragon", "World Legacy Guardragon"])[2]
    assert ftk(["Black Metal Dragon", "One for One"])[2]
    return True


def test_ftk():
    # Tests all
    assert one_card()
    assert two_card()
    assert vs_nibiru()
    assert incorrect_ftks()
    assert three_card()

    print("All tests pass")


test_ftk()
