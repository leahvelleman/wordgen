import pytest
from src.state import State, EPSILON

def test_state_can_add_arc():
    s = State()
    s.add_arc("a", "x", s)

def test_state_can_give_ouput_on_arc():
    s = State()
    s.add_arc("a", "x", s)
    assert s.follow("a") == ("x", s)

def test_state_can_have_epsilon_transitions():
    s = State()
    t = State()
    s.add_arc("a", "x", s)
    s.add_arc(EPSILON, "y", t)
    assert s.follow("z") == ("y", t)

def test_take_epsilon_transitions_only_when_theres_no_other_choice():
    s = State()
    t = State()
    s.add_arc("a", "x", s)
    s.add_arc(EPSILON, "y", t)
    assert s.follow("a") == ("x", s)

def test_error_if_you_cant_accept_a_symbol():
    s = State()
    s.add_arc("a", "x", s)
    with pytest.raises(KeyError):
        s.follow("b")

