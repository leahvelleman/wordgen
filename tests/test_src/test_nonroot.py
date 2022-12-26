from src.nonroot import Nonroot
from src.sounds import Sounds
from src.word import Word

def test_affixes_have_kind():
    a = Nonroot(kind="affix", side="left")
    assert a.kind == "affix"

def test_affixes_have_side():
    a = Nonroot(kind="affix", side="left")
    assert a.side == "left"

def test_empty_affixes_are_empty():
    a = Nonroot(kind="affix", side="left")
    assert a.segments == []

def test_affixes_contain_sounds():
    a = Nonroot(kind="affix", side="left", segments=[Sounds("ch", "tʃ")])
    assert type(a.segments[0]) == Sounds

