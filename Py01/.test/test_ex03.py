from ex03 import recorsive_sqrt

def test1_ex03():
    result = recorsive_sqrt(0)
    expected = 0
    assert result == expected, f'Error: expected {expected}, got {result}'

def test2_ex03():
    result = recorsive_sqrt(1)
    expected = 1
    assert result == expected, f'Error: expected {expected}, got {result}'

def test3_ex03():
    result = recorsive_sqrt(5)
    expected = 0
    assert result == expected, f'Error: expected {expected}, got {result}'

def test4_ex03():
    result = recorsive_sqrt(16)
    expected = 4
    assert result == expected, f'Error: expected {expected}, got {result}'

def test5_ex03():
    result = recorsive_sqrt(36)
    expected = 6
    assert result == expected, f'Error: expected {expected}, got {result}'