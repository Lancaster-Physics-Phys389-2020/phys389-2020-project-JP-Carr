from analytical_E_levels import analytical_E as aE
from random import randint

def test_analytical_E0():
    assert isinstance(aE(randint(0,10)),float)