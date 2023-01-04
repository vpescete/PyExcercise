from ex06 import print_type_int
import sys

def test1_ex06():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_type_int(10)
    assert captured_output.getvalue() == "10\n<class 'int'>\n"

    sys.stdout = sys.__stdout__

def test2_ex06():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_type_int(8)
    assert captured_output.getvalue() == "8\n<class 'int'>\n"

    sys.stdout = sys.__stdout__

def test3_ex06():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_type_int('ciao')
    assert captured_output.getvalue() == "ciao\n<class 'str'>\n"

    sys.stdout = sys.__stdout__