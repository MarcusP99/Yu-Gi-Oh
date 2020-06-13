from combinations import ftk


# One card FTKs
def one_card():
    assert ftk(["Black Metal Dragon"], [])[0]
    assert ftk(["Starliege Seyfert"], [])[0]
    return True


# Hands that ftk with two cards
def two_card():
    assert ftk(["White Rose Dragon", "Red Rose Dragon"], [])[0]
    assert ftk(["Dragunity Phalanx", "World Legacy Guardragon"], [])[0]
    assert ftk(["Omni Dragon Brotaur", "Rokket Tracer"], [])[0]
    assert ftk(["Quick Launch", "Quick Launch"], [])[0]
    assert ftk(["Quick Launch", "Effect Veiler"], [])[0]
    assert ftk(["Rokket Tracer", "Rokket Tracer"], [])[0]
    assert ftk(["Quick Launch", "Ash Blossom & Joyous Springs"], [])[0]
    assert ftk(["Rokket Tracer", "Black Garden"], [])[0]
    assert ftk(["Quick Launch", "Black Garden"], [])[0]
    return True


# Hands that ftk with three cards
def three_card():
    assert ftk(["Boot Sector Launch", "Exploderokket Dragon", "Effect Veiler"], [])[0]
    assert ftk(["Boot Sector Launch", "Rokket Tracer", "Effect Veiler"], [])[0]
    return True


# FTKs we have recognised give a wrong result (we need to fix)
def incorrect_ftks():
    assert ftk(["Dragon Shrine", "Dragon Shrine"], [])[0]
    assert ftk(["One for One", "Spell"], [])[0]
    assert ftk(["Chaos Space", "Spell"], [])[0]
    return True


# FTKs that we haven't recognised vs nibiru (we need to fix)
def incorrect_nibiru_ftks():
    assert not ftk(["Black Metal Dragon", "Rokket Tracer", "Dragon Shrine"], [])[2]
    assert not ftk(["Black Metal Dragon", "Black Dragon Collapserpent", "Dragon Shrine"], [])[2]
    return True


# Hands that can combo through nibiru
def vs_nibiru():
    assert ftk(["Black Metal Dragon", "World Legacy Guardragon"], [])[2]
    assert ftk(["Black Metal Dragon", "One for One"], [])[2]
    assert not ftk(["Black Metal Dragon", "Noctovision Dragon", "Rokket Tracer"], [])[2]
    assert not ftk(["Black Metal Dragon", "Black Dragon Collapserpent"], [])[2]
    assert ftk(["Rokket Tracer", "Rokket Tracer", "World Legacy Guardragon"], [])[2]
    assert ftk(["Starliege Seyfert", "Rokket Tracer", "Rokket Tracer"], [])[2]
    assert ftk(["Starliege Seyfert", "Absorouter Dragon", "Rokket Tracer"], [])[2]
    return True


def test_ftk():
    # Tests all
    assert one_card()
    assert two_card()
    assert vs_nibiru()
    assert incorrect_ftks()
    assert three_card()
    assert incorrect_nibiru_ftks()

    print("All tests pass")


test_ftk()
