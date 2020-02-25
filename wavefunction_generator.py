from potential import potential 
from potential import V
from QHO import quantum_harmonic_oscilator as QHO
import numpy as np
import matplotlib as plt

potential_start=0
potential_end=1
delta_x=1/1000

trial_E=1

V=potential(potential_start, potential_end)
electron=QHO(potential_start+2*delta_x,trial_E,delta_x)

#print(electron.position)

def WF_attempt(trial_E=None):
    
    while electron.position<potential_end:
        #v0,v1,v2=potential.V(electron.position),potential.V(electron.position-delta_x),potential.V(electron.position-2*delta_x)        
        v0=V(electron.position)
        print(v0)
        electron.next_wavevalue(v0, v1, v2)
        electron.position+=delta_x
        print(electron.position)
    else:
        print("Done")
        
WF_attempt()