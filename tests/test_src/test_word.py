from src.word import Word
from src.root import Root
from src.affix import Affix
from src.inflection import Inflection
from src.sounds import Sounds

def test_left_affixing_with_segments_works():
    segs = [Sounds("ch", "tʃ")]
    a = Affix(side="left", segments=segs, gloss="test")
    r = Root(segments=[Sounds("a", "a")], gloss="gloss")
    w = Word([r])
    w.affix(a)
    assert w.morphemes[0].segments == segs

def test_right_affixing_with_segments_works():
    segs = [Sounds("ch", "tʃ")]
    a = Affix(side="right", segments=segs, gloss="test")
    r = Root(segments=[Sounds("a", "a")], gloss="gloss")
    w = Word([r])
    w.affix(a)
    assert w.morphemes[-1].segments == segs

def test_you_can_apply_an_inflection():
    w = Word([])
    i = Inflection(side="left", gloss="test")
    assert w.apply(i)

def test_applying_an_inflection_creates_an_affix():
    w = Word([])
    i = Inflection(side="left", gloss="test")
    w2 = w.apply(i)
    assert type(w2.morphemes[0]) == Affix

def test_applying_an_inflection_leaves_original_word_unchanged():
    w = Word([])
    assert len(w.morphemes) == 0
    i = Inflection(side="left", gloss="test")
    w.apply(i)
    assert len(w.morphemes) == 0

def test_subclassing():
    dep_suffix = Inflection(side="right", gloss="test", segments=[Sounds(ipa="h")])
    class Noun(Word):
        def dep(self):
            return self.apply(dep_suffix)
    
    w = Noun()
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
    
    w = Noun([Root(Sounds(ipa="kora"))])
    assert w.dep().morphemes[-1].segments[0].ipa == "h"


# applying an inflection puts the created nonroot on the correct side
