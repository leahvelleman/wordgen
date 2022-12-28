import pytest

from src.root import Root
from src.sounds import Sounds
from src.word import Word

def test_roots_have_kind():
    r = Root(gloss="foo")
    assert r.kind == "root"

def test_roots_do_not_have_side():
    with pytest.raises(Exception):
        r = Root(gloss="foo", side="left")

def test_roots_contain_sounds():
    r = Root(gloss="foo", ipa="tʃ", spelling="ch")
    assert type(r.segments[0]) == Sounds

def test_root_ipa_property():
    s = [Sounds(ipa="ab", spelling="12"), Sounds(ipa="cd", spelling="34")]
    r = Root(gloss="foo", segments=s)
    assert r.ipa == "abcd"

def test_root_spelling_property():
    s = [Sounds(ipa="ab", spelling="12"), Sounds(ipa="cd", spelling="34")]
    r = Root(gloss="foo", segments=s)
    assert r.spelling == "1234"

def test_root_requires_a_gloss():
    with pytest.raises(Exception):
        r = Root(ipa="fu", spelling="foo")

def test_initialize_root_with_list_of_sounds():
    s = Sounds(ipa="fu", spelling="foo")
    r = Root(gloss="something", segments=[s])
    assert r.segments[0] == s

def test_initialize_root_with_kwargs():
    r = Root(gloss="something", ipa="fu", spelling="foo")
    assert r.segments[0].ipa == "fu"

