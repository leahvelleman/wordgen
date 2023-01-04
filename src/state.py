EPSILON = -38473298487238

class State():
    def __init__(self):
        self.arcs = {}
    
    def add_arc(self, input_symbol, output_symbol, state):
        self.arcs[input_symbol] = (output_symbol, state)

    def follow(self, input_symbol):
        if input_symbol in self.arcs:
            return self.arcs[input_symbol]
        elif EPSILON in self.arcs:
            return self.arcs[EPSILON]
        else:
            raise KeyError