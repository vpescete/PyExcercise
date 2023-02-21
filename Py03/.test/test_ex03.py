from ex03 import dict_to_list
import sys

def test1_ex03():
	assert dict_to_list({'c': 1, 'i': 1, 'a': 1, 'o': 1}) == [('c', 1), ('i', 1), ('a', 1), ('o', 1)]

def test2_ex03():
	assert dict_to_list({'c': 2, 'i': 2, 'a': 2, 'o': 2, ' ': 2, 'm': 1, 'e': 1, 's': 1, 't': 1, '?': 1}) == [('c', 2), ('i', 2), ('a', 2), ('o', 2), (' ', 2), ('m', 1), ('e', 1), ('s', 1), ('t', 1), ('?', 1)]

def test3_ex03():
	assert dict_to_list({' ': 1}) == [(' ', 1)]

def test4_ex03():
	assert dict_to_list({'c': 2, 'i': 2, 'a': 2, 'o': 2, ' ': 2, 'm': 1, 'e': 1, 't': 1, 'L': 1, 'p': 1, 'S': 1, ',': 1, '?': 1}) == [('c', 2), ('i', 2), ('a', 2), ('o', 2), (' ', 2), ('m', 1), ('e', 1), ('t', 1), ('L', 1), ('p', 1), ('S', 1), (',', 1), ('?', 1)]
