from plates import is_valid

def test_too_short():
    assert is_valid('a') == False

def test_too_long():
    assert is_valid('abcdefghij') == False

def test_just_right():
    assert is_valid('CS50') == True

def test_wrong_num():
    assert is_valid('CS05') == False

def test_num_placement():
    assert is_valid('AAA22A') == False
    assert is_valid('AAA222') == True

def test_alphabetical():
    assert is_valid('AA') == True

def test_alphanumeric():
    assert is_valid('1B') == False
    assert is_valid('A1') == False

def test_non_alphas():
    assert is_valid('PI3.14') == False