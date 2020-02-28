from scipy import constants as const
import numpy as np

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
        """
        print(format((12-10*self.f_n(potential_minus1)) * self.wavefunction[-1],"1.1E"))
        print(format(self.f_n(potential_minus2) * self.wavefunction[-2],"1.1E"))
        print(format(self.f_n(potential0),"1.1E"))
        print("----------------------------------------------------------------------")
        """
        psi=((12-10*self.f_n(potential_minus1)) * self.wavefunction[-1]-  self.f_n(potential_minus2) * self.wavefunction[-2])    /self.f_n(potential0)
      #  psi=2*self.wavefunction[-1]*(1-5*self.delta_x)
        #print(psi)
        self.wavefunction=np.append(self.wavefunction,psi)
    #    print (psi)
        #print(self.wavefunction)
        return psi
    #--------------------------------------------------------------------

    def next_wavevalue2(self,potential0,potential_minus1,potential_minus2):
        return


"""
x=quantum_harmonic_oscilator(0.5, 1, 0.005)
v=V(0,1)
v0,v1,v2=v.V(x.position),v.V(x.position-x.delta_x),v.V(x.position-2*x.delta_x)
#print(v0,v1,v2)


print(x.next_wavevalue(v0,v1,v2))
"""