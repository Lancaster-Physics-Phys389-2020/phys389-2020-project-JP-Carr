import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from error import error
from probability_plotter import normalise
from analytical_psi import psi as analytical_psi


norm=True   # should wavefunction be plotted as normalised?
comparison=True # display comparison plot?


"""
Plots the wavefunction data produced by "wavefunction_generator.py"
"""
try:
    wave_function_csv="wavefunctions_N=1000.csv"
    
except:
    error("Unable to load"+str(wave_function_csv))
data=pd.read_csv("wavefunctions\\"+str(wave_function_csv))  #create dataframe from csv
N=len(data)

x_array=np.linspace(-1/2,1/2,N)  # positional array


plt.figure("Wavefunctions (N={})".format(N))
    
plt.xlabel(r"$\tilde{x}$")
plt.ylabel(r"$\psi(\tilde{x})$")
  
i=1 
while 1:
    try:
        psi=data[str(i)]
        norm_psi=psi*normalise(data[str(i)], x_array)  #normalise wavefunction
        if norm==True:
            plt.plot(x_array,norm_psi, label="n="+str(i))
        else:
            plt.plot(x_array,psi, label="n="+str(i))
        i+=1
    except:
        break
    
plt.tick_params(which='both',direction='in',right=True,top=True)
plt.legend()



if comparison==True:
    """
    Plots difference between the numerically calculated wavefunction and it's analytical counterpart
    """
    plt.figure("Wavefunctions comparison")
    i=1 
    while i==1:
        try:
            psi_diff=np.array(data[str(i)]*normalise(data[str(i)], x_array) /analytical_psi(x_array, i, 1))
            plt.plot(np.delete(x_array,[999]),np.log10(np.delete(psi_diff, [999])),label="n="+str(i))
            i+=1
        except:
            break
plt.xlabel(r"$\tilde{x}$")
plt.ylabel(r"$log(\psi_{numerical}/\psi_{analytical})$")
plt.show()