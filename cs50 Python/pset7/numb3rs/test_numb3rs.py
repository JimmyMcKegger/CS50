from numb3rs import validate

def test_validate():
    assert validate('0.0.0.0') == True
    assert validate('0.1.2.3.4') == False
    assert validate('1.1.1.1') == True
    assert validate('2.3.4.5.') == False
    assert validate('1.2000.3.4') == False
    assert validate('1.2.300.4') == False
    assert validate('1.2.3.4') == True
    assert validate('a.b.c.d') == False
    assert validate("255.255.255.255") == True
    assert validate("256.300.400.500") == False

def test_validate_format():
    assert validate("a") == False
    assert validate("123") == False

def test_validate_byte():
    assert validate("4?") == False
    assert validate('1,two,three,four') == False
    assert validate('o.1.2.3') == False

def main():
    test_validate()
    test_validate_format()
    test_validate_byte()

if __name__ == "__main__":
    main()
