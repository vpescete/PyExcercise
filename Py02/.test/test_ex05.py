from ex05 import ft_upCase

def upCase(string):
    return (string.upper())

def test1_ex00():
	str_1 = "ciao"
	str_2 = "ciao"

	assert ft_upCase(str_1) == upCase(str_2)
 
def test1_ex01():
	str_1 = "ciao CIAO"
	str_2 = "ciao CIAO"

	assert ft_upCase(str_1) == upCase(str_2)