from src.sounds import Sounds

class Morpheme():
    def __init__(self):
        ...

    def initialize_segments(self, segments, **kwargs):
        if segments is not None:
            if all([type(m) is Sounds for m in segments]):
                self.segments = segments
            else:
                raise Exception
        else:
            self.segments = [Sounds(**kwargs)]

    @property
    def ipa(self):
        return "".join([s.ipa for s in self.segments])

    @property
    def spelling(self):
        return "".join([s.spelling for s in self.segments])