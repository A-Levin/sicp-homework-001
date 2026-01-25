import sys
sys.path.insert(0, '.')

from min import min

def test_min_positive():
    assert min(7, 12) == 7
    assert min(12, 7) == 7

def test_min_negative():
    assert min(-3, -7) == -7
    assert min(-7, -3) == -7

def test_min_mixed():
    assert min(-5, 5) == -5
    assert min(0, -1) == -1

def test_min_equal():
    result = min(5, 5)
    assert result == 5

def test_min_floats():
    assert min(3.14, 2.71) == 2.71
    assert min(0.1, 0.2) == 0.1
