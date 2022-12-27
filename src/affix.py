from src.morpheme import Morpheme

class Affix(Morpheme):
    def __init__(self, side, gloss, segments=None, **kwargs):
        self.kind = "affix"
        self.side = side
        self.gloss = gloss
        self.initialize_segments(segments, **kwargs)