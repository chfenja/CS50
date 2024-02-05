from twttr import shorten


def test_word():
    assert shorten("CS50") == "CS50"
    assert shorten("----") == "----"
    assert shorten("Twitter") == "Twttr"


def test_sentence():
    assert shorten("What's your name?") == "Wht's yr nm?"
