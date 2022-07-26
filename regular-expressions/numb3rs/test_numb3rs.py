from numb3rs import validate

def test_validate():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("12.25.37.49") == True
    assert validate("-2.45.65.88") == False
    assert validate("66.78.256.320") == False

def test_validate_string():
    assert validate("") == False
    assert validate("cat") == False


