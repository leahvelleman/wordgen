from src.affix import Affix

class Inflection():
    def __init__(self, side, gloss, segments=None, function=None, **kwargs):
        self.side = side
        self.segments = segments
        self.function = function
        self.gloss = gloss
        self.kwargs = kwargs

    def realize(self, word):
        if self.function:
            args = {
                **self.function(word), 
                "side": self.side,
                "gloss": self.gloss
            }
            return Affix(**args)
        else:
            return Affix(
                side = self.side,
                gloss = self.gloss,
                segments = self.segments,
                **self.kwargs
            )   
