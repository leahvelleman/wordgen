from src.morpheme import Morpheme

class Root(Morpheme):
    def __init__(self, gloss, segments=None, **kwargs):
        self.kind = "root"
        self.gloss = gloss
        self.initialize_segments(segments, **kwargs)