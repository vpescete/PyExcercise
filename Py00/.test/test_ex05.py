from ex05 import mod_nb

def test1_ex05():
  result = mod_nb(10, 5)
  expected = 0
  assert result == expected, f'Error: expected {expected}, got {result}'

def test2_ex05():
  result = mod_nb(2, 2)
  expected = 0
  assert result == expected, f'Error: expected {expected}, got {result}'

def test3_ex05():
  result = mod_nb(5, 10)
  expected = 5
  assert result == expected, f'Error: expected {expected}, got {result}'