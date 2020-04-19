from quantum_particle import q_particle
import numpy

steps=100
electron=q_particle(2,1,1,steps)


def test_next_psi0():
    """
    Tests if the results from next_psi are numpy floats
    """
    assert isinstance(electron.next_psi(1*numpy.ones(steps), 2),numpy.float64)
    
def test_next_psi1():
    """
    Tests if the returned value of next_psi are less than 1, given a potential of depth 1
    """
    assert electron.next_psi(1*numpy.ones(steps),2)<1
                        
