import pytest

from src.root import Root
from src.sounds import Sounds
from src.word import Word

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

