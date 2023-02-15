from ex03 import ft_isUppercase
import sys

def test1_ex00():
	assert ft_isUppercase("ciao") == False
 
def test1_ex01():
	assert ft_isUppercase(15) == False

def test1_ex02():
	assert ft_isUppercase("ciao come stai") == False

def test1_ex03():
	assert ft_isUppercase(str(15)) == False
 
def test1_ex04():
	assert ft_isUppercase("CIAO") == True