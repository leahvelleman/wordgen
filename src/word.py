from copy import deepcopy

class Word():
    def __init__(self, morphemes=None):
        self.morphemes = morphemes or []

    def affix(self, a):
        if a.side == "left":
            self.morphemes.insert(0, a)
        else:
            self.morphemes.append(a)

    def apply(self, inflection):
        copy = deepcopy(self)
        nonroot = inflection.realize(self)
        self.affix(nonroot)
        return self