from ex10 import ft_sqrt
import sys

def test1_ex10():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    ft_sqrt(81)
    assert captured_output.getvalue() == "9\n<class 'int'>\n"

    sys.stdout = sys.__stdout__

def test2_ex10():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    ft_sqrt(100)
    assert captured_output.getvalue() == "10\n<class 'int'>\n"

    sys.stdout = sys.__stdout__

def test3_ex10():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    ft_sqrt(9874432)
    assert captured_output.getvalue() == "3142.36089588704\n<class 'float'>\n"

    sys.stdout = sys.__stdout__