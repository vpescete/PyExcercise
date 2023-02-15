from ex12 import ft_lowCase

def lowCase(string):
    return (string.lower())

def test1_ex00():
	str_1 = "ciao"
	str_2 = "ciao"

	assert ft_lowCase(str_1) == lowCase(str_2)
 
def test1_ex01():
	str_1 = "ciao CIAO"
	str_2 = "ciao CIAO"

	assert ft_lowCase(str_1) == lowCase(str_2)