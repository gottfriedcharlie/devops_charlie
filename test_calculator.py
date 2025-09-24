from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_add2():
    calc = Calculator()
    assert calc.add(-2, -3) == -5

def test_add3():
    calc = Calculator()
    assert calc.add(6, 7) == 13