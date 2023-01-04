from ex00 import print_int
import sys

def test1_ex00():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_int(81)
    assert captured_output.getvalue() == "81\n<class 'str'>\n"

    sys.stdout = sys.__stdout__

def test2_ex00():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_int(100)
    assert captured_output.getvalue() == "100\n<class 'str'>\n"

    sys.stdout = sys.__stdout__

def test3_ex00():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_int('9874432')
    assert captured_output.getvalue() == "9874432\n<class 'str'>\n"

    sys.stdout = sys.__stdout__