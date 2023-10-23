from ex01 import fizzbuzz
import sys

def fizzbuzz0():
	l = ""
	x = range(100)
	for i in x:
		if i % 3 == 0 and i % 5 == 0:
			l += "fizzbuzz" + "\n"
		elif i % 3 == 0:
			l += "fizz" + "\n"
		elif i % 5 == 0:
			l += "buzz" + "\n"
		else:
			l += str(i) + "\n"
	return l
    
def test1_ex00():

	from io import StringIO
	captured_output = StringIO()
	sys.stdout = captured_output
 
	fizzbuzz()
	# Ripristina sys.stdout al suo valore originale
	sys.stdout = sys.__stdout__

	# Rimuovi l'ultimo carattere di nuova riga
	output = captured_output.getvalue()
	if output.endswith('\n'):
		output = output[:-1]

	assert output == fizzbuzz0()
