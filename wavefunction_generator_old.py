from potential_class import potential 
from QHO import quantum_harmonic_oscilator as QHO
import numpy as np
import matplotlib.pyplot as plt
import plotter

potential_start=-1
potential_end=1
step_no=200
delta_x=(potential_end-potential_start)/step_no
position_array=np.linspace(potential_start,potential_end-delta_x,step_no)
#print(position_array)
E=1
psi_tolerance=1E-50

#epos=[-1]
"""
well=potential(potential_start, potential_end)
electron=QHO(potential_start+2*delta_x,trial_E,delta_x)
"""
#print(electron.position)

def WF_attempt(trial_E=E):
    well=potential(potential_start, potential_end,form="ISW",k=1)
    electron=QHO(potential_start+2*delta_x,trial_E,delta_x)
    print("New wavefunction")
    
    while electron.position<potential_end:
        #v0,v1,v2=potential.V(electron.position),potential.V(electron.position-delta_x),potential.V(electron.position-2*delta_x)        
        v0,v1,v2=well.V(electron.position),well.V(electron.position-delta_x),well.V(electron.position-2*delta_x)
    #    print("g_n={},{},{}".format(electron.g_n(v0),electron.g_n(v1),electron.g_n(v2)))
       # print(v0,v1,v2)
        electron.next_wavevalue(v0, v1, v2)
       # print(electron.wavefunction)
        
        electron.position+=delta_x
   #     print("-----------------------------------")
       # epos.append(electron.position)
        #print(electron.position)

    else:
       # print("Done")
        print(electron.wavefunction)
        plotter.plot(position_array, electron.wavefunction, "title", "x_lab", "y_lab")
        return electron.wavefunction[-1]
        
     
        
def E_finder(start_E):
    
    
    
    trial_E=start_E
    delta_E=trial_E/2
    best_psi=1E5000
    
    while abs(best_psi)>psi_tolerance:
        
        print("loop")
        print("best ψ={}".format(best_psi))
        trial_E+=delta_E
        test_wave=WF_attempt(trial_E)
        
        if np.sign(test_wave)!=np.sign(best_psi):
            delta_E=-delta_E/2
            print("Overstep")
            best_psi=test_wave
            
        elif abs(test_wave)>abs(best_psi):
            delta_E=-delta_E
            print("Reversing direction")
        else:
            print("Improvement")
            best_psi=test_wave
    else:
        print("Value found: E = {}\n ψ(L) = {}".format(trial_E,best_psi))
        return trial_E
        
        
        
        
WF_attempt()

#E_finder(E)

#print(len(position_array),len(epos),len(electron.wavefunction))
#print(position_array[-1],electron.wavefunction[-1])

#vlist=[well.V(i) for i in position_array]

#plotter.plot(position_array, vlist, "title", "x_lab", "y_lab")
#plt.plot(position_array,electron.wavefunction)
#plt.show()