from bank import value


def test_hello():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"


def test_h():
    assert value("how are you doing?") == "$20"
    assert value("how is it going?") == "$20"
    assert value("How's life?") == "$20"


def test_clean():
    assert value("What's happening?") == "$100"
    assert value("what's good?") == "$100"
