from src.sounds import Sounds

def test_sounds_have_kind():
    s = Sounds()
    assert s.kind == "sounds"

def test_sounds_have_spelling():
    s = Sounds("abc")
    assert s.spelling == "abc"

def test_sounds_have_ipa():
    s = Sounds(ipa="tʃ")
    assert s.ipa == "tʃ"