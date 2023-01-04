from ex08 import print_str
import sys

def test1_ex08():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_str(10)
    assert captured_output.getvalue() == "10\n<class 'str'>\n"

    sys.stdout = sys.__stdout__

def test2_ex08():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_str('9')
    assert captured_output.getvalue() == "9\n<class 'str'>\n"

    sys.stdout = sys.__stdout__

def test3_ex08():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_str('ciao')
    assert captured_output.getvalue() == "ciao\n<class 'str'>\n"

    sys.stdout = sys.__stdout__