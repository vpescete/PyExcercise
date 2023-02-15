from ex13 import ft_isAlphabetic
import sys

def test1_ex00():
	assert ft_isAlphabetic("ciao") == True
 
def test1_ex01():
	assert ft_isAlphabetic(15) == False

def test1_ex02():
	assert ft_isAlphabetic("ciao come stai") == False

def test1_ex03():
	assert ft_isAlphabetic(str(15)) == False
 
def test1_ex04():
	assert ft_isAlphabetic("CIAO") == True