from src.affix import Affix
from src.sounds import Sounds
from src.word import Word

def test_affixes_have_kind():
    a = Affix(gloss="foo", side="left")
    assert a.kind == "affix"

def test_affixes_have_side():
    a = Affix(gloss="foo", side="left")
    assert a.side == "left"

def test_affixes_contain_sounds():
    a = Affix(gloss="foo", side="left", ipa="tʃ", spelling="ch")
    assert type(a.segments[0]) == Sounds

