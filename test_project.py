from project import validate_amount, validate_date, validate_name


def test_validate_amount():
    assert validate_amount("123.12") is True
    assert validate_amount("123") is True
    assert validate_amount("hundred") is False
    assert validate_amount("123,123") is False



def test_validate_date():
    assert validate_date("17-11-2024") is True
    assert validate_date("17-17-2024") is False
    assert validate_date("40-11-2024") is False
    assert validate_date("testing") is False
    assert validate_date("17112024") is False


def test_validate_name():
    assert validate_name("ABCDsd") is True
    assert validate_name("ABCDsd123") is False
    assert validate_name("ABCDsd$#") is False
    assert validate_name("ABCD EFG") is True
    assert validate_name("ABCD,EFG") is True
