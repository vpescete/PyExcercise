from ex04 import ft_isLowercase
import sys

def test1_ex00():
	assert ft_isLowercase("ciao") == True
 
def test1_ex01():
	assert ft_isLowercase(15) == False

def test1_ex02():
	assert ft_isLowercase("ciao come stai") == False

def test1_ex03():
	assert ft_isLowercase(str(15)) == False
 
def test1_ex04():
	assert ft_isLowercase("CIAO") == False