import pytest
from queue import q

def test_init():
    x = q.Queue([1, 2])
    print(x.items)
    x.add(3)
    assert x.items == [1, 2, 3]
    assert x.remove() == 1
    assert x.items == [2, 3]

    y = q.Queue()
    assert y.items == []
    y.remove()
    assert y.items == []
    