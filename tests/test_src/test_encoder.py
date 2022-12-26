from src.sounds import Sounds
from src.encoder import Encoder

def test_sounds_are_serializable():
    s = Sounds("ch", ipa="tʃ")
    e = Encoder()
    assert e.encode(s) == '{"kind": "sounds", "spelling": "ch", "ipa": "tʃ"}'

