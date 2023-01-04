from ex04 import recursive_power

def test1_ex04():
    result = recursive_power(5, 0)
    expected = 1
    assert result == expected, f'Error: expected {expected}, got {result}'

def test2_ex04():
    result = recursive_power(1, -5)
    expected = 0
    assert result == expected, f'Error: expected {expected}, got {result}'

def test3_ex04():
    result = recursive_power(5, 2)
    expected = 25
    assert result == expected, f'Error: expected {expected}, got {result}'

def test4_ex04():
    result = recursive_power(-4, 2)
    expected = 16
    assert result == expected, f'Error: expected {expected}, got {result}'

def test5_ex04():
    result = recursive_power(-2, 3)
    expected = -8
    assert result == expected, f'Error: expected {expected}, got {result}'