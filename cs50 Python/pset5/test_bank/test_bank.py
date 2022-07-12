from bank import value

def test_bank_zero():
    assert value('Hello') == 0

def test_bank_twenty():
    assert value('Howdy') == 20

def test_bank_hundo():
    assert value("Bonjour") == 100
