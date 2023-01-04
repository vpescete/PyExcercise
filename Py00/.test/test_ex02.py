from ex02 import prod_nb

def test1_ex02():
  result = prod_nb(1, 2)
  expected = 2
  assert result == expected, f'Error: expected {expected}, got {result}'

def test2_ex02():
  result = prod_nb(2, 2)
  expected = 4
  assert result == expected, f'Error: expected {expected}, got {result}'

def test3_ex02():
  result = prod_nb(1, -1)
  expected = -1
  assert result == expected, f'Error: expected {expected}, got {result}'