from ex09 import print_type_float_or_int
import sys

def test1_ex09():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_type_float_or_int(10)
    assert captured_output.getvalue() == "10\n<class 'int'>\n"

    sys.stdout = sys.__stdout__

def test2_ex09():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_type_float_or_int(10.5)
    assert captured_output.getvalue() == "10.5\n<class 'float'>\n"

    sys.stdout = sys.__stdout__

def test3_ex09():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_type_float_or_int(9874432)
    assert captured_output.getvalue() == "9874432\n<class 'int'>\n"

    sys.stdout = sys.__stdout__