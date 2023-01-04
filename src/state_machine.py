from src.state import State, EPSILON

class StateMachine():
    def __init__(self):
        self.states = {}
    
    def add_state(self, n):
        if n in self.states:
            raise Exception
        self.states[n] = State()