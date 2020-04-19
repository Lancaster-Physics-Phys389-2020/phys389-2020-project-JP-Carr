import wavefunction_generator as wg
from numpy.random import rand


def test_turn_points0():
    """ 
    Tests if the calculated number of turning points is an integer
    """
    assert isinstance(wg.turn_points(rand(1,10)[0]),int)
    
def test_turn_points1():
    """ 
    Tests if the calculated number of turning points is not negative
    """
    assert wg.turn_points(rand(1,10)[0])>=0