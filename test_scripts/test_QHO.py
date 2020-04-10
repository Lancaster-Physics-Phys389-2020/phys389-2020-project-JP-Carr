from QHO import quantum_harmonic_oscilator
import numpy

steps=100
QHO=quantum_harmonic_oscilator(2,1,1,steps)


def test_next_psi0():
    assert isinstance(QHO.next_psi(1*numpy.ones(steps), 2),numpy.float64)
    
def test_next_psi1():
    assert QHO.next_psi(1*numpy.ones(steps),2)<1
                        
