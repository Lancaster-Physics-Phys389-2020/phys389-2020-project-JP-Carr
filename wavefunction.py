from numerov import numerov
from scipy import constants as const
import numpy as np
#x=numerov(0,0.0001,1,12,0,0.001)

start_energy=1
initial_conditions=(0,1E-10)
#wavefunction=[i for i in initial_conditions]
L=1
iterations=1000
delta_x=L/iterations
tolerance=1E-20 

def potential(x,k=1):
    return 1/2*k*x**2

def function_value(edge0,edge1,energy,x):    
    return numerov(edge0,edge1,1,energy,potential(x),delta_x)

#print (function_value(initial_conditions[0],initial_conditions[1],start_energy,0))
    
def find_E():
    trial_energy=start_energy
    energy_step=start_energy/10
    best_wave=1E100
    tolerance =1E-50
    
    
    while best_wave>tolerance:
        
        trial_energy=+energy_step
        wave_test=function_value(initial_conditions[0],initial_conditions[1], trial_energy, 0)
        print("ψ = {}".format(wave_test))
        if np.sign(wave_test)!=np.sign(best_wave):
            energy_step=-energy_step/2
            print("Overstep")
            best_wave=function_value(initial_conditions[0],initial_conditions[1], trial_energy, 0)
        elif abs(wave_test)>abs(best_wave):
            energy_step=-energy_step
            print("Reversing direction")
        
    
    print(trial_energy)
    
    
#find_E()
#print(type(function_value(initial_conditions[0],initial_conditions[1], start_energy, 0)))