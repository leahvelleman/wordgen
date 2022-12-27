from src.sounds import Sounds

class Root():
    def __init__(self, gloss, segments=None, **kwargs):
        self.kind = "root"
        self.gloss = gloss
        self.initialize_segments(segments, **kwargs)

    def initialize_segments(self, segments, **kwargs):
        if segments is not None:
            if all([type(m) is Sounds for m in segments]):
                self.segments = segments
            else:
                raise Exception
        else:
            self.segments = [Sounds(**kwargs)]