from probability_plotter import normalise as norm
import numpy as np

x=np.array([i for i in range (-10,10)])
y=-x**2

def test_normalise0():
    assert isinstance(norm(y,x),np.float64)
    
