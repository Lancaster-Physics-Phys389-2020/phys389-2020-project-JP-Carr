from potential_class import potential 
import numpy
import pytest

steps=10
V=potential(steps)
print (V.nu())
print (type(V.nu()))

def test_depth():
   # assert 1==1
    assert isinstance(V.V_depth(),numpy.int32)
    
def test_nu1():
    assert len(V.nu())==steps
def test_nu2():
    assert isinstance(V.nu(),numpy.ndarray)    
    
