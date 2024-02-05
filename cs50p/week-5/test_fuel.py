from pytest import raises
from fuel import convert, gauge


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("2/4") == 50
    assert convert("99/100") == 99


def test_convert_zero_exceptions():
    with raises(ZeroDivisionError):
        convert("1/0")


def test_convert_invalid_input_negative_numbers():
    with raises(ValueError):
        convert("-1/2")
    with raises(ValueError):
        convert("1/-2")


def test_convert_invalid_input_numerator_greater_than_denominator():
    with raises(ValueError):
        convert("5/4")


def test_convert_invalid_input_non_integer():
    with raises(ValueError):
        convert("a/b")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
