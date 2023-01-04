from ex01 import print_max
import sys

def test1_ex01():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_max(81, 90)
    assert captured_output.getvalue() == "Il numero maggiore è : 90\n"

    sys.stdout = sys.__stdout__

def test2_ex01():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_max(101, 1)
    assert captured_output.getvalue() == "Il numero maggiore è : 101\n"

    sys.stdout = sys.__stdout__

def test3_ex01():

    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_max(-283920, -9484849343)
    assert captured_output.getvalue() == "Il numero maggiore è : -283920\n"

    sys.stdout = sys.__stdout__