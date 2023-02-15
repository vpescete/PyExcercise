from ex02 import ft_isString
import sys

def test1_ex00():
	assert ft_isString("ciao") == True
 
def test1_ex01():
	assert ft_isString(15) == False

def test1_ex02():
	assert ft_isString("ciao come stai") == True

def test1_ex03():
	assert ft_isString(str(15)) == True