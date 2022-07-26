from seasons import birth_date
import pytest

def test_birth_date():
    with pytest.raises(SystemExit):
        birth_date("July 3, 1978") == None
        birth_date("cat") == None
