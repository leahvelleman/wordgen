from src.word import Word
from src.root import Root
from src.nonroot import Nonroot
from src.inflection import Inflection
from src.sounds import Sounds

def test_left_affixing_with_segments_works():
    segs = [Sounds("ch", "tʃ")]
    a = Nonroot(kind="affix", side="left", segments=segs)
    r = Root(segments=[Sounds("a", "a")], gloss="gloss")
    w = Word([r])
    w.affix(a)
    assert w.morphemes[0].segments == segs

def test_right_affixing_with_segments_works():
    segs = [Sounds("ch", "tʃ")]
    a = Nonroot(kind="affix", side="right", segments=segs)
    r = Root(segments=[Sounds("a", "a")], gloss="gloss")
    w = Word([r])
    w.affix(a)
    assert w.morphemes[-1].segments == segs

def test_you_can_apply_an_inflection():
    w = Word([])
    i = Inflection(side="left", kind="affix")
    assert w.apply(i)

def test_applying_an_inflection_creates_a_nonroot():
    w = Word([])
    i = Inflection(side="left", kind="affix")
    w2 = w.apply(i)
    assert type(w2.morphemes[0]) == Nonroot

def test_applying_an_inflection_leaves_original_word_unchanged():
    w = Word([])
    assert len(w.morphemes) == 0
    i = Inflection(side="left", kind="affix")
    w.apply(i)
    assert len(w.morphemes) == 0

def test_subclassing():
    dep_suffix = Inflection(kind="affix", side="right", segments="h")
    class Noun(Word):
        def dep(self):
            return self.apply(dep_suffix)
    
    w = Noun([Root("kora")])
    assert w.dep().morphemes[-1].segments == "h"

def test_subclassing_with_function():
    dep_suffix = Inflection(
        kind="affix", 
        side="right", 
        function=lambda w: {"segments": "h"}
    )
    class Noun(Word):
        def dep(self):
            return self.apply(dep_suffix)
    
    w = Noun([Root(Sounds(ipa="kora"))])
    assert w.dep().morphemes[-1].segments == "h"


# applying an inflection puts the created nonroot on the correct side
