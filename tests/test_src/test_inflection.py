from src.inflection import Inflection
from src.nonroot import Nonroot

def test_Inflection_can_have_function():
    i = Inflection(side="left", kind="affix", function=lambda w: None)
    assert i.function

def test_realizing_an_Inflection_creates_an_affix():
    i = Inflection(side="left", kind="affix")
    affix = i.realize([])
    assert type(affix) == Nonroot

def test_realizing_an_Inflection_calls_its_function(mocker):
    stub = mocker.stub(name="realization_function")
    i = Inflection(side="left", kind="affix", function=stub)
    affix = i.realize([])
    stub.assert_called_once_with([]) 

def test_realizing_an_Inflection_with_a_function_creates_an_affix():
    f = lambda w: {}
    i = Inflection(side="left", kind="affix", function=f)
    affix = i.realize([])
    assert type(affix) == Nonroot

def test_function_Inflections_still_inherit_side():
    f = lambda w: {"side": "right"}
    i = Inflection(side="left", kind="affix", function=f)
    affix = i.realize([])
    assert affix.side == "left"

def test_Inflections_are_comparable():
    i_1 = Inflection(side="left", kind="affix")
    i_2 = Inflection(side="left", kind="affix")
    assert i_1 != i_2

def test_affixes_know_their_type():
    i = Inflection(side="left", kind="affix")
    affix = i.realize([])
    assert affix.affixtype == i
