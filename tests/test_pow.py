import sys
sys.path.insert(0, '.')

from pow import pow

def test_pow_basic():
    assert pow(2, 3) == 8
    assert pow(3, 2) == 9

def test_pow_zero_exp():
    assert pow(5, 0) == 1
    assert pow(100, 0) == 1

def test_pow_one_exp():
    assert pow(7, 1) == 7
    assert pow(123, 1) == 123

def test_pow_large():
    assert pow(2, 10) == 1024
    assert pow(3, 5) == 243

def test_pow_one_base():
    assert pow(1, 100) == 1

def test_pow_zero_base():
    assert pow(0, 5) == 0
