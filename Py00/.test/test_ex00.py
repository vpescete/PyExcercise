from ex00 import somma_nb

def test1_ex00():
  result = somma_nb(1, 2)
  expected = 3
  assert result == expected, f'Error: expected {expected}, got {result}'

def test2_ex00():
  result = somma_nb(2, 2)
  expected = 4
  assert result == expected, f'Error: expected {expected}, got {result}'

def test3_ex00():
  result = somma_nb(1, -1)
  expected = 0
  assert result == expected, f'Error: expected {expected}, got {result}'