from copy import deepcopy
import re
from src.root import Root
from src.affix import Affix

class Word():
    def __init__(self, definition, morphemes=None, **kwargs):
        self.kind = "word"
        self.definition = definition
        self.initialize_morphemes(morphemes, **kwargs)

    def initialize_morphemes(self, morphemes, **kwargs):
        if morphemes is not None:
            if all([type(m) in [Root, Affix] for m in morphemes]):
                self.morphemes = morphemes
            else:
                raise Exception
        else:
            self.morphemes = [Root(**kwargs)]

    def affix(self, a):
        if a.side == "left":
            self.morphemes.insert(0, a)
        else:
            self.morphemes.append(a)

    def apply(self, inflection):
        copy = deepcopy(self)
        nonroot = inflection.realize(copy)
        copy.affix(nonroot)
        return copy

    @property
    def ipa(self):
        return "".join([m.ipa for m in self.morphemes])

    @property
    def spelling(self):
        return "".join([m.spelling for m in self.morphemes])

    def find(self, needle):
        haystack = self.ipa
        return re.search(needle, haystack).span()

    