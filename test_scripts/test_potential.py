from potential_class import potential 
import numpy

steps=10
V=potential(steps)
print (V.nu())
print (type(V.nu()))

def test_depth():
    """
    Tests if the returned value from V_depth is a numpy integer
    """
    assert isinstance(V.V_depth(),numpy.int32)
    
def test_nu0():
    """
    Tests if the array for the nondimensionalised potential is the same size as 
    the number of integration steps
    """
    assert len(V.nu())==steps
def test_nu1():
    """
    Tests if the returned object for the the nondimensionalised potential is a 
    numpy array
    """
    assert isinstance(V.nu(),numpy.ndarray)    
    
