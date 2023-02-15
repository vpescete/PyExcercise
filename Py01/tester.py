import pytest

if __name__ == '__main__':
  print('EX00')
  pytest.main(['-v', '--tb=short', '--no-header', './.test/test_ex00.py'])
  print('EX01')
  pytest.main(['-v', '--tb=short', '--no-header', './.test/test_ex01.py'])
  print('EX02')
  pytest.main(['-v', '--tb=short', '--no-header', './.test/test_ex02.py'])
  print('EX03')
  pytest.main(['-v', '--tb=short', '--no-header', './.test/test_ex03.py'])
  print('EX04')
  pytest.main(['-v', '--tb=short', '--no-header', './.test/test_ex04.py'])