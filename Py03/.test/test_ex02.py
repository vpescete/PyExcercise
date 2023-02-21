from ex02 import count_char

def test1_ex02():
	assert count_char("ciao") == {'c': 1, 'i': 1, 'a': 1, 'o': 1}

def test2_ex02():
	assert count_char("ciao come stai?") == {'c': 2, 'i': 2, 'a': 2, 'o': 2, ' ': 2, 'm': 1, 'e': 1, 's': 1, 't': 1, '?': 1}

def test3_ex02():
	assert count_char(" ") == {' ': 1}

def test4_ex02():
	assert count_char("ciao, come te L4 p4SS1 ?") == {'c': 2, 'i': 1, 'a': 1, 'o': 2, ' ': 5, 'm': 1, 'e': 2, 't': 1, 'L': 1, '4': 2, 'p': 1, 'S': 2, '1': 1, ',': 1, '?': 1}
