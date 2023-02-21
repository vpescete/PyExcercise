from ex01 import split_ascii
import sys

def test1_ex01():	
	assert split_ascii("c1a0, come te L4 p4SS1 ?") == [['c', 'a', 'c', 'o', 'm', 'e', 't', 'e', 'L', 'p', 'S', 'S'], ['1', '0', '4', '4', '1'], [',', ' ', ' ', ' ', ' ', ' ', '?']]

def test2_ex01():
	assert split_ascii("ciao come stai?") == [['c', 'i', 'a', 'o', 'c', 'o', 'm', 'e', 's', 't', 'a', 'i'], [], [' ', ' ','?']]

def test3_ex01():
	assert split_ascii(" ") == [[], [], [' ']]

def test4_ex01():
	assert split_ascii("ciao, come te L4 p4SS11 ?") == [['c', 'i', 'a', 'o', 'c', 'o', 'm', 'e', 't', 'e', 'L', 'p', 'S', 'S'], ['4','4', '1', '1'], [',', ' ', ' ', ' ', ' ', ' ', '?']]