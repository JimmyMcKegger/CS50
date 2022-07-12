from um import count

def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_in_word():
    assert count("yummy") == 0

def test_space():
    assert count(",um.") == 1

def test_case():
    assert count("um, UM, um") == 3