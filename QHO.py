from scipy import constants as const
import numpy as np
from error import error
"""
class quantum_harmonic_oscilator:
    def __init__(self,start_position,trial_energy,delta_x,mass=const.m_e):
        self.position=start_position
        self.delta_x=delta_x
        self.energy=trial_energy
        self.mass=mass
        self.position_array=np.array([start_position])
        self.wavefunction=np.array([0,1E-4])
        
        
    #Numerov method------------------------------------------------------
        
    def g_n(self,potential):
       # print("V = {}".format(potential))
     #   print(potential,(2*self.mass/(const.hbar**2))*(self.energy-potential))
      #  print("---------------------------------")
        return (2*self.mass/(const.hbar**2))*(self.energy-potential)
   
    def f_n(self,potential):
        return 1+self.g_n(potential)*((self.delta_x**2)/12)
    
    def next_wavevalue(self,potential0,potential_minus1,potential_minus2): #potential0 for current value of x

        print(format((12-10*self.f_n(potential_minus1)) * self.wavefunction[-1],"1.1E"))
        print(format(self.f_n(potential_minus2) * self.wavefunction[-2],"1.1E"))
        print(format(self.f_n(potential0),"1.1E"))
        print("----------------------------------------------------------------------")

        psi=((12-10*self.f_n(potential_minus1)) * self.wavefunction[-1]-  self.f_n(potential_minus2) * self.wavefunction[-2])    /self.f_n(potential0)
      #  psi=2*self.wavefunction[-1]*(1-5*self.delta_x)
        #print(psi)
        self.wavefunction=np.append(self.wavefunction,psi)
    #    print (psi)
        #print(self.wavefunction)
        return psi
    #--------------------------------------------------------------------
"""

class quantum_harmonic_oscilator:
    def __init__(self,trial_energy,well_depth,length,steps,start_position=0,mass=const.m_e):
        """
        Initialises QHO

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
        self.gamma_sq=200#2*self.mass*(self.length**2)*self.well_depth/(const.hbar**2)
      #  print(self.mass,self.length,self.well_depth,const.hbar)
     #   print("γ² = "+str(self.gamma_sq))
        
    def next_psi(self,nu_array,n):  #n - iteration starts at 2
        
        for nu in nu_array:
            if self.epsilon-nu<0:
                print(self.epsilon,nu)
                error("epsilon - nu < 0")
        else:
       #     print(self.gamma,np.power(self.epsilon-nu_array,0.5))
            k_sq=self.gamma_sq*(self.epsilon-nu_array)
         #   print(k_sq)
        
     #   print(self.l**2,k_sq[n-1],self.wavefunction[n-1])
        
        a=2*(1-5/12*(self.l**2)*k_sq[n-1])*self.wavefunction[n-1]
      #  print(a)
        b=(1+1/12*self.l**2*k_sq[n-2])*self.wavefunction[n-2]
        c=1+1/12*self.l**2*k_sq[n]
        
        psi_n=(a-b)/c
        
        self.wavefunction=np.append(self.wavefunction,psi_n)
      #  print("ψ {}".format(len(self.wavefunction)))


















"""
x=quantum_harmonic_oscilator(0.5, 1, 0.005)
v=V(0,1)
v0,v1,v2=v.V(x.position),v.V(x.position-x.delta_x),v.V(x.position-2*x.delta_x)
#print(v0,v1,v2)


print(x.next_wavevalue(v0,v1,v2))

"""