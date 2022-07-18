from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    small_jar = Jar(5)
    assert small_jar.capacity == 5
    with pytest.raises(ValueError):
        negative_jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(25)
