import pytest

from src.word import Word
from src.root import Root
from src.affix import Affix
from src.inflection import Inflection
from src.sounds import Sounds

def test_words_require_definitions():
    with pytest.raises(Exception):
        w = Word(morphemes=[])

def test_left_affixing_with_segments_works():
    a = Affix(side="left", spelling="ch", ipa="ch", gloss="test")
    r = Root(spelling="a", ipa="a", gloss="gloss")
    w = Word(definition="foo", morphemes=[r])
    w.affix(a)
    assert w.morphemes[0].segments[0].spelling == "ch"

def test_right_affixing_with_segments_works():
    a = Affix(side="right", spelling="ch", ipa="ch", gloss="test")
    r = Root(spelling="a", ipa="a", gloss="gloss")
    w = Word(definition="foo", morphemes=[r])
    w.affix(a)
    assert w.morphemes[-1].segments[0].spelling == "ch"

def test_create_word_from_kwargs():
    w = Word(definition="a", spelling="b", ipa="c", gloss="d")
    assert w.morphemes[0].segments[0].ipa == "c"

def test_you_can_apply_an_inflection():
    w = Word(spelling="a", ipa="b", gloss="c", definition="d")
    i = Inflection(side="left", gloss="test")
    assert w.apply(i)

def test_applying_an_inflection_creates_an_affix():
    w = Word(spelling="a", ipa="b", gloss="c", definition="d")
    i = Inflection(side="left", gloss="test")
    w2 = w.apply(i)
    assert type(w2.morphemes[0]) == Affix

def test_applying_an_inflection_leaves_original_word_unchanged():
    w = Word(spelling="a", ipa="b", gloss="c", definition="d")
    assert len(w.morphemes) == 1
    i = Inflection(side="left", gloss="test")
    w.apply(i)
    assert len(w.morphemes) == 1

def test_ipa_method_gives_concatenated_ipa_strings():
    w = Word(morphemes=[
             Root(spelling="ab", ipa="12", gloss="wx"),
             Affix(side="right", spelling="cd", ipa="34", gloss="yz")],
        definition="foo")
    assert w.ipa == "1234"

def test_spelling_method_gives_concatenated_spelling_strings():
    w = Word(morphemes=[
             Root(spelling="ab", ipa="12", gloss="wx"),
             Affix(side="right", spelling="cd", ipa="34", gloss="yz")],
        definition="foo")
    assert w.spelling == "abcd"

def test_find_works_on_monomorphemic_word():
    w = Word(
        morphemes=[
            Root(spelling="", ipa="abcde", gloss="")
        ],
        definition="foo"
    )
    assert w.find("bc") == (1,3)

def test_find_works_on_multimorphemic_word():
    w = Word(
        morphemes=[
            Root(spelling="", ipa="ab", gloss=""),
            Affix(side="right", spelling="", ipa="cde", gloss="")
        ],
        definition="foo"
    )
    assert w.find("bc") == (1,3)

def test_subclassing():
    dep_suffix = Inflection(side="right", gloss="test", segments=[Sounds(ipa="h")])
    class Noun(Word):
        def dep(self):
            return self.apply(dep_suffix)
    
    w = Noun(spelling="a", ipa="b", gloss="c", definition="d")
    assert w.dep().morphemes[-1].segments[0].ipa == "h"

def test_subclassing_with_function():
    dep_suffix = Inflection(
        side="right", 
        gloss="test",
        function=lambda w: {"ipa": "h"}
    )
    class Noun(Word):
        def dep(self):
            return self.apply(dep_suffix)
    
    w = Noun(spelling="a", ipa="b", gloss="c", definition="d")
    assert w.dep().morphemes[-1].segments[0].ipa == "h"




# applying an inflection puts the created nonroot on the correct side
