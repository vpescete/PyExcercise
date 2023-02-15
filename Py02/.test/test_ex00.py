from ex00 import printFrom0ToNb
import sys

def printfrom0(s):
  l = ""
  x = range(s)
  for i in x:
    l += str(i) + "\n"  
  return l
      
    

def test1_ex00():

	from io import StringIO
	captured_output = StringIO()
	sys.stdout = captured_output
 
	printFrom0ToNb(11)
	assert captured_output.getvalue() == printfrom0(11)
 
def test2_ex00():

	from io import StringIO
	captured_output = StringIO()
	sys.stdout = captured_output
 
	printFrom0ToNb(100);
	assert captured_output.getvalue() == printfrom0(100)
 
def test3_ex00():

	from io import StringIO
	captured_output = StringIO()
	sys.stdout = captured_output
 
	printFrom0ToNb(114343);
	assert captured_output.getvalue() == printfrom0(114343)
 
def test4_ex00():

	from io import StringIO
	captured_output = StringIO()
	sys.stdout = captured_output
 
	printFrom0ToNb(-12);
	assert captured_output.getvalue() == printfrom0(-12)