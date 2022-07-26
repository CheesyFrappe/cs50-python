from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(14)
    assert jar.capacity == 14
    with pytest.raises(ValueError):
        jar = Jar(-2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(11)
        jar.deposit(-1)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(6)
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(5)
