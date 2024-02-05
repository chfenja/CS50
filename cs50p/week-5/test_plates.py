from plates import is_valid


def test_start_two_letters():
    assert is_valid("CS50")
    assert not is_valid("C50")
    assert not is_valid("500")


def test_max_char():
    assert not is_valid("OUTATIME")
    assert not is_valid("numerous")


def test_min_char():
    assert not is_valid("C")
    assert not is_valid("s")


def test_num_end():
    assert not is_valid("CS50P")
    assert is_valid("AAA222")
    assert not is_valid("AAA22A")


def test_no_zero_first():
    assert not is_valid("CS05")
    assert is_valid("CS50")


def test_no_symbols():
    assert not is_valid("PI3.14")
    assert not is_valid("who ?")
    assert not is_valid("What!")
