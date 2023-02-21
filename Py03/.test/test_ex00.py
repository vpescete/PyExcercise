from ex00 import split_list
import sys

def test1_ex00():	
	assert split_list("ciao") == ['c', 'i', 'a', 'o']

def test2_ex00():
	assert split_list("ciao come stai?") == ['c', 'i', 'a', 'o', 'c', 'o', 'm', 'e', 's', 't', 'a', 'i']

def test3_ex00():
	assert split_list("ciao, come te L4 p4SS1 ?") == ['c', 'i', 'a', 'o', 'c', 'o', 'm', 'e', 't', 'e', 'L', 'p', 'S', 'S']

def test4_ex00():
	assert split_list("ciao, come te L4 p4SS1111111111111111111111111 ?") == ['c', 'i', 'a', 'o', 'c', 'o', 'm', 'e', 't', 'e', 'L', 'p', 'S', 'S']	