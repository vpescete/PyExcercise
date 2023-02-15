from ex10 import ft_isLowercase

def isLo(str):
    if type(str) != type(""):
        return False
    i = 0
    while i < len(str):
        if (not(str[i] >= 'a' and str[i] <= 'z')):
            i += 1
        else:
            break
    if i != len(str):
      return (False)
    else:
      return (True)
  
def test1_ex00():
	str_1 = "ciao"

	assert ft_isLowercase(str_1) == ft_isLowercase(str_1)
 
def test1_ex01():
	str_1 = "ciao CIAO"

	assert ft_isLowercase(str_1) == ft_isLowercase(str_1)