from potential_class import potential 
from QHO import quantum_harmonic_oscilator 
import numpy as np
import matplotlib.pyplot as plt
import plotter
import copy
import time

start=time.time()

N=1000
well_length=1
x_array=np.linspace(-well_length/2,well_length/2,N)
start_E=0.95#065197799
psi_tolerance=1E-12


V=potential(N)


def WF_attempt(trial_E=start_E):
    QHO=quantum_harmonic_oscilator(trial_E,V.V_depth(),well_length,N)
  #  print("New wavefunction")
    
    for i in range(2,N):
    #    print("Loop  i = {}".format(i))
        QHO.next_psi(V.nu(), i)
    
    
   # plt.plot(x_array,QHO.wavefunction)
    return QHO.wavefunction[-1]
    
def E_finder(inital_E=start_E):
    trial_E=inital_E
    delta_E=trial_E/100
    best_psi=WF_attempt(trial_E)
    last_psi=copy.deepcopy(best_psi)
    
    while abs(best_psi)>psi_tolerance:
        print("-----------------------")
       # print("loop")
        trial_E+=delta_E
        test_wave=WF_attempt(trial_E)
        print("last ψ={}     trial ψ={}".format(last_psi,test_wave))
        print("E = "+str(trial_E))
        
        
        if abs(test_wave)>abs(best_psi):
            delta_E=-delta_E
            print("Worse - Reversing direction")            

        else:
            print("Improvement")
            best_psi=test_wave
            
            if np.sign(test_wave)!=np.sign(last_psi):
                delta_E=delta_E/2
                print("Overstep")
                #best_psi=test_wave
        last_psi=copy.deepcopy(test_wave)
    else:
        print("Value found: E = {}\n ψ(L) = {}".format(trial_E,best_psi))
        return trial_E
    
    
#WF_attempt()
    
E_finder()



print("Time elapsed = {}s".format(time.time()-start))