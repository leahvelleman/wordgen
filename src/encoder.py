from json import JSONEncoder

class Encoder(JSONEncoder):
    def __init__(self):
        super().__init__(ensure_ascii=False)
        
    def default(self, o):
        return o.__dict__