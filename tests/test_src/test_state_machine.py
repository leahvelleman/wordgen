import pytest
from src.state import State, EPSILON
from src.state_machine import StateMachine


def test_adding_a_state_by_number_creates_a_state_object():
    sm = StateMachine()
    sm.add_state(12)
    assert type(sm.states[12]) == State

def test_cant_add_a_state_twice():
    sm = StateMachine()
    sm.add_state(12)
    with pytest.raises(Exception):
        sm.add_state(12)

