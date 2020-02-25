#from potential import potential as V
from scipy import constants as const

class quantum_harmonic_oscilator:
    def __init__(self,position,potential,trial_energy,mass=const.m_e):
        self.position=position
        self.potential=potential
        self.energy=trial_energy
        self.mass=mass
        self.wavefunction=[0,10E-10]
        
        
        