from potential_class import potential 
from QHO import quantum_harmonic_oscilator 
import numpy as np
import matplotlib.pyplot as plt
import plotter
import copy
import multiprocessing
import time
import pandas as pd


start=time.time()

N=round(1000/2) #endures N is always an int
well_length=1
x_array=np.linspace(-well_length/2,well_length/2,N)
start_E=0.21#0.95#065197799
E_list=[]
psi_tolerance=1E-12



V=potential(N)

def turn_points(array):
    n=0
    for i in range(1,len(array)-1):
        if (array[i]<array[i-1] and array[i]<array[i+1]) or (array[i]>array[i-1] and array[i]>array[i+1]):
            n+=1
    return n


def WF_attempt(trial_E=start_E):
    global out 
    QHO=quantum_harmonic_oscilator(trial_E,V.V_depth(),well_length,N)
  #  print("New wavefunction")
    
    for i in range(2,N):
    #    print("Loop  i = {}".format(i))
        QHO.next_psi(V.nu(), i)
    
    
   # plt.plot(x_array,QHO.wavefunction)
    out=QHO.wavefunction
    return QHO.wavefunction
    
def E_finder(inital_E=start_E):
    trial_E=inital_E
    delta_E=trial_E/100
    best_psi=WF_attempt(trial_E)[-1]
    last_psi=copy.deepcopy(best_psi)
    
    while abs(best_psi)>psi_tolerance:
        print("-----------------------")
       # print("loop")
        trial_E+=delta_E
        test_wave=WF_attempt(trial_E)
        test_wave_L=test_wave[-1]
        print("last ψ={}     trial ψ={}".format(last_psi,test_wave_L))
        print("E = "+str(trial_E))
        
        
        if abs(test_wave_L)>abs(best_psi):
            delta_E=-delta_E
            print("Worse - Reversing direction")            

        else:
            print("Improvement")
            best_psi=test_wave_L
            
            if np.sign(test_wave_L)!=np.sign(last_psi):
                delta_E=delta_E/2
                print("Overstep")
                #best_psi=test_wave_L
        last_psi=copy.deepcopy(test_wave_L)
    else:
        print("Value found: E = {}\n ψ(L) = {}".format(trial_E,best_psi))  #    ADD IN TURNING POINTS AND DATAFRAME
      #  print(turn_points(last_psi))
        return trial_E,test_wave,turn_points(test_wave)
    
    
#WF_attempt()
    
a,b,c=E_finder()
print(c)

plt.plot(x_array,b)
print("Time elapsed = {}s".format(time.time()-start))