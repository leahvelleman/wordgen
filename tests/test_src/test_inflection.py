from src.inflection import Inflection
from src.affix import Affix

def test_Inflection_can_have_function():
    i = Inflection(side="left", gloss="test", function=lambda w: None)
    assert i.function

def test_inflection_can_use_kwargs():
    i = Inflection(side="left", gloss="test", ipa="fu", spelling="foo")

def test_realizing_an_Inflection_creates_an_affix():
    i = Inflection(side="left", gloss="test")
    affix = i.realize([])
    assert type(affix) == Affix

def test_realizing_an_inflection_passes_on_its_kwargs():
    i = Inflection(side="left", gloss="test", ipa="fu", spelling="foo")
    affix = i.realize([])
    assert affix.segments[0].ipa == "fu"

def test_realizing_an_Inflection_calls_its_function(mocker):
    stub = mocker.stub(name="realization_function")
    i = Inflection(side="left", gloss="test", function=stub)
    affix = i.realize([])
    stub.assert_called_once_with([]) 

def test_realizing_an_Inflection_with_a_function_creates_an_affix():
    f = lambda w: {}
    i = Inflection(side="left", gloss="test", function=f)
    affix = i.realize([])
    assert type(affix) == Affix

def test_function_Inflections_still_inherit_side():
    f = lambda w: {"side": "right"}
    i = Inflection(side="left", gloss="test", function=f)
    affix = i.realize([])
    assert affix.side == "left"

def test_Inflections_are_comparable():
    i_1 = Inflection(side="left", gloss="test")
    i_2 = Inflection(side="left", gloss="test")
    assert i_1 != i_2
