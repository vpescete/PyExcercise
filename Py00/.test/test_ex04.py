from ex04 import div_nb

def test1_ex04():
  result = div_nb(10, 5)
  expected = 2
  assert result == expected, f'Error: expected {expected}, got {result}'

def test2_ex04():
  result = div_nb(2, 2)
  expected = 1
  assert result == expected, f'Error: expected {expected}, got {result}'

def test3_ex04():
  result = div_nb(5, 10)
  expected = 0.5
  assert result == expected, f'Error: expected {expected}, got {result}'