import sys
sys.path.insert(0, '.')

from max import max

def test_max_positive():
    assert max(7, 12) == 12
    assert max(12, 7) == 12

def test_max_negative():
    assert max(-3, -7) == -3
    assert max(-7, -3) == -3

def test_max_mixed():
    assert max(-5, 5) == 5
    assert max(0, -1) == 0

def test_max_equal():
    result = max(5, 5)
    assert result == 5

def test_max_floats():
    assert max(3.14, 2.71) == 3.14
    assert max(0.1, 0.2) == 0.2
