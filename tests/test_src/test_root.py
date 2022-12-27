from src.root import Root
from src.sounds import Sounds
from src.word import Word

def test_initialize_root_with_list_of_sounds():
    s = Sounds()
    r = Root([s])
    assert r.segments[0] == s