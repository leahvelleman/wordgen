class Nonroot():
    def __init__(self, side, kind, affixtype=None, segments=None, gloss=""):
        self.kind = kind
        self.side = side
        self.affixtype = affixtype
        self.segments = segments or []
        self.gloss = gloss
