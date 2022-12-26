class Root():
    def __init__(self, segments=None):
        self.kind = "root"
        self.segments = segments or []