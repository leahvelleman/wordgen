from src.nonroot import Nonroot

class Inflection():
    def __init__(self, side, kind, segments=None, function=None, gloss=""):
        self.side = side
        self.kind = kind
        self.segments = segments or []
        self.function = function
        self.gloss = gloss

    def realize(self, word):
        if self.function:
            args = {
                **self.function(word), 
                "side": self.side,
                "kind": self.kind,
                "affixtype": self
            }
            return Nonroot(**args)
        else:
            return Nonroot(
                side = self.side,
                kind = self.kind,
                segments = self.segments,
                gloss = self.gloss,
                affixtype = self
            )   
