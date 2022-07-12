from fuel import convert, gauge
import pytest

def test_correct_input():
    assert convert('0/4') == 0 and gauge(0) == 'E'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('3/4') == 75 and gauge(75) == '75%'
    assert convert('99/100') == 99 and gauge(99) == 'F'
    assert convert('7/7') == 100 and gauge(100) == 'F'

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert('1/cat')
        convert("dog/3")

def main():
    test_zero_division_error()
    test_value_error()
    test_correct_input()

if __name__ == "__main__":
    main()