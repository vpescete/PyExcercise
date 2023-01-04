from ex02 import fibonacci

def test1_ex02():
    result = fibonacci(0)
    expected = 0
    assert result == expected, f'Error: expected {expected}, got {result}'

def test2_ex02():
    result = fibonacci(1)
    expected = 1
    assert result == expected, f'Error: expected {expected}, got {result}'

def test3_ex02():
    result = fibonacci(5)
    expected = 5
    assert result == expected, f'Error: expected {expected}, got {result}'

def test4_ex02():
    result = fibonacci(7)
    expected = 13
    assert result == expected, f'Error: expected {expected}, got {result}'

def test5_ex02():
    result = fibonacci(11)
    expected = 89
    assert result == expected, f'Error: expected {expected}, got {result}'