from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("cat")
        convert("12:00 PM - 05:00 AM")

def test_convert_invalid_hour():
    with pytest.raises(ValueError):
        convert("12:00 PM to 13:00 AM")
        convert("13 PM to 17 PM")
        convert("13 AM to 12 PM")

def test_convert_invalid_minute():
    with pytest.raises(ValueError):
        convert("09:65 AM to 13:00 PM")
        convert("14:76 AM to 12 PM")
