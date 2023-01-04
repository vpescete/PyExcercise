from ex01 import diff_nb

def test1_ex01():
  result = diff_nb(1, 2)
  expected = -1
  assert result == expected, f'Error: expected {expected}, got {result}'

def test2_ex01():
  result = diff_nb(2, 2)
  expected = 0
  assert result == expected, f'Error: expected {expected}, got {result}'

def test3_ex01():
  result = diff_nb(1, -1)
  expected = 2
  assert result == expected, f'Error: expected {expected}, got {result}'

def test4_ex01():
  result = diff_nb(10, 5)
  expected = 5
  assert result == expected, f'Error: expected {expected}, got {result}'