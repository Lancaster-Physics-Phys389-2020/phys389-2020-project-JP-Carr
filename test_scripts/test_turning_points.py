import wavefunction_generator as wg
from numpy.random import rand


def test_turn_points0():
    assert isinstance(wg.turn_points(rand(1,10)[0]),int)
    
def test_turn_points1():
    assert wg.turn_points(rand(1,10)[0])>=0