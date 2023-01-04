from ex07 import print_bool
import sys

def test1_ex07():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_bool(True)
    assert captured_output.getvalue() == "True\n<class 'bool'>\n"

    sys.stdout = sys.__stdout__

def test2_ex07():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_bool(False)
    assert captured_output.getvalue() == "False\n<class 'bool'>\n"

    sys.stdout = sys.__stdout__
