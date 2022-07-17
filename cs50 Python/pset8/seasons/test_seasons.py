from seasons import season
import pytest

def test_last_year():
    assert season("2021-07-17") == "Five hundred twenty-five thousand, six hundred minutes"

def test_wrong_format():
    with pytest.raises(SystemExit):
        assert season("25 July, 1999")
        assert season("July 14th, 1987")
        assert season("1 July '08")
        assert season("2020 01 01")
