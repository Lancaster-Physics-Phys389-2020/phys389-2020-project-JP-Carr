from potential_class import potential 
from quantum_particle import q_particle 
import numpy as np

import copy
import pandas as pd
from error import error
import time



well_length=1
E_list=[0.9,0.8,0.5,0.2,-0.2,-0.7,-1.4,-2.1,-2.9,-3.9]
psi_tolerance=1E-12
psi_dict={}


if __name__=="__main__":
    import time
    start=time.time()
    N=round(50*20) #endures N is always an int
    x_array=np.linspace(-well_length/2,well_length/2,N)
    V=potential(N)


def turn_points(array):
    """
    Counts the number of turning points in an array

    Parameters
    ----------
    array : numpy.ndarray
        Array of values to be processed.

    Returns
    -------
    n : int
        Number of turning points.

    """
    n=0
    for i in range(1,len(array)-1):
        if (array[i]<array[i-1] and array[i]<array[i+1]) or (array[i]>array[i-1] and array[i]>array[i+1]):
            n+=1
    return n


def WF_attempt(trial_E):
    """
    Creates a Quantum Harmonic Oscillator object and attempts to 
    produce a valid wavefunction using Numerov's formula

    Parameters
    ----------
    trial_E : float, optional
        The dimentionless energy for this attempt.

    Returns
    -------
    electron.wavefunction: numpy.ndarray
        Final wavefunction attempt.

    """
    electron=q_particle(trial_E,V.V_depth(),well_length,N)

    for i in range(2,N):
        electron.next_psi(V.nu(), i)
    wave=copy.deepcopy(electron.wavefunction)
    del electron
    return wave
    
def E_finder(inital_E):
    trial_E=inital_E
    delta_E=trial_E/100
    best_psi=WF_attempt(trial_E)[-1]
    last_psi=copy.deepcopy(best_psi)
    
    while abs(best_psi)>psi_tolerance:

        trial_E+=delta_E
        test_wave=WF_attempt(trial_E)
        test_wave_L=test_wave[-1]

        
        
        if abs(test_wave_L)>abs(best_psi):
            delta_E=-delta_E
     #       print("Worse - Reversing direction")            

        else:
     #       print("Improvement")
            best_psi=test_wave_L
            
            if np.sign(test_wave_L)!=np.sign(last_psi):
                delta_E=delta_E/2
       #         print("Overstep")

        last_psi=copy.deepcopy(test_wave_L)
    else:
        n=turn_points(test_wave)
        print("Value found (n={}): \nE = {}\n ψ(L) = {}\n".format(n,trial_E,best_psi))  #    ADD IN TURNING POINTS AND DATAFRAME
        energy_dict["n"].append(n)
        energy_dict["epsilon"].append(trial_E)
        psi_dict[str(n)]=test_wave
        return trial_E,test_wave,n
    
    
def run(i):
    global N
    global x_array
    global V
    global energy_dict
    start=time.time()
    N=round(i*50)
    x_array=np.linspace(-well_length/2,well_length/2,N)
    V=potential(N)
    energy_dict={"n":[], "epsilon":[]}
    print("running N={}".format(N))
    

    for energy in E_list:
        E,psi,n=E_finder(energy)
    
    
    energy_df=pd.DataFrame(data=energy_dict)
    psi_df=pd.DataFrame(data=psi_dict)
    row_limit=len(E_list)
    if energy_df.shape[0]>row_limit: #catches extra iterations
        rfd=[i for i in range(row_limit,energy_df.shape[0])] #Rows For Deletion
        energy_df.drop(rfd,inplace=True)
    
    energy_df.index.name=str(N)
    psi_df
    try:
        pd.DataFrame.to_csv(energy_df, "energy_levels\\{}\\energy_levels_N={}.csv".format(V.form,N))
        print("Saved \"energy_levels_N={}.csv\"".format(N))
    except:
        print("energy_levels\\{}\\energy_levels_N={}.csv".format(V.form,N))
        error("Unable to save \"energy_levels_N={}.csv\"".format(N),False)
    del energy_df
    try:
        pd.DataFrame.to_csv(psi_df, "wavefunctions\\{}\\wavefunctions_N={}.csv".format(V.form,N))
        print("Saved \"wavefunctions_N={}.csv\"".format(N))
    except:
        error("Unable to save \"wavefunctions_N={}.csv\"".format(N),False)
    del psi_df
    
    return N,time.time()-start
        
if __name__=="__main__":
    run(N/50)
    print("Time elapsed = {}s".format(round(time.time()-start,2)))
    print("\a")