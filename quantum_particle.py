from scipy import constants as const
import numpy as np
from error import error


class q_particle:
    def __init__(self,trial_energy,well_depth,length,steps,start_position=0,mass=const.m_e):
        """
        Initialises a particle

        Parameters
        ----------
        trial_energy : float
            Energy of oscillator for current attempt.
        well_depth : float
            Minimum potential of the well.
        length : float
            Distance over which the wavefunction is to be calculated.
        steps : int
            Number of integration points used.
        start_position : TYPE, optional
            DESCRIPTION. The default is 0.
        mass : float, optional
            DESCRIPTION. The default is const.m_e.

        Returns
        -------
        None.

        """
        self.trial_energy=trial_energy
        self.well_depth=well_depth
        self.steps=steps
        self.start_position=start_position
        self.mass=mass
        self.wavefunction=np.array([0,1E-5])
        self.length=length
        
        #UNITLESS VARIABLES
        self.epsilon=self.trial_energy/self.well_depth    #unitless energy
        self.l=1/(self.steps-1)                          #step length
        self.gamma_sq=200                                #unitless constant

        
    def next_psi(self,nu_array,n):  #n - iteration starts at 2
        for nu in nu_array:
            if self.epsilon-nu<0:
                print(self.epsilon,nu)
                error("epsilon - nu < 0")
        else:
            k_sq=self.gamma_sq*(self.epsilon-nu_array)
        
        a=2*(1-5/12*(self.l**2)*k_sq[n-1])*self.wavefunction[n-1]

        b=(1+1/12*self.l**2*k_sq[n-2])*self.wavefunction[n-2]
        c=1+1/12*self.l**2*k_sq[n]
        
        psi_n=(a-b)/c
        
        self.wavefunction=np.append(self.wavefunction,psi_n)
        return psi_n

