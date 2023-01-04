from ex03 import div_int_nb

def test1_ex03():
  result = div_int_nb(10, 5)
  expected = 2
  assert result == expected, f'Error: expected {expected}, got {result}'

def test2_ex03():
  result = div_int_nb(2, 2)
  expected = 1
  assert result == expected, f'Error: expected {expected}, got {result}'

def test3_ex03():
  result = div_int_nb(5, 10)
  expected = 0
  assert result == expected, f'Error: expected {expected}, got {result}'