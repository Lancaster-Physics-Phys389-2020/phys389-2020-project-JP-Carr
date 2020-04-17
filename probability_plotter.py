import numpy as np
import matplotlib.pyplot as plt
#from os import listdir
import pandas as pd
from error import error

def normalise(y_array,x_array):
    """
    Produces the normalisation constant for a given array

    Parameters
    ----------
    y_array : numpy.ndarray
        Array of y-axis values to be normalised.
    x_array : numpy.ndarray
        Array of corresponding x-axis values.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    integral=np.trapz(y_array**2,x=x_array)
    const=1/integral
    return const**0.5

if __name__=="__main__":
    """
    Plots the normalised probability density when script is run directly
    """

    try:
        wave_function_csv="wavefunctions_N=1000.csv"
        
    except:
        error("Unable to load"+str(wave_function_csv))
    data=pd.read_csv("wavefunctions\\"+str(wave_function_csv))
    N=len(data)
    
    position_array=np.linspace(-1/2,1/2,N)
    
    
    plt.figure("Probability (N={})".format(N))
        
    plt.xlabel(r"$\tilde{x}$")
    plt.ylabel(r"$|\psi(\tilde{x})|^2$")
    i=1 
    while 1:
        try:      
            prob=((normalise(data[str(i)],position_array))*data[str(i)])**2   # Normalises probability density
            plt.plot(position_array,prob, label="n="+str(i))
            i+=1
        except:
            break
        
    plt.tick_params(which='both',direction='in',right=True,top=True)
    plt.legend()
    plt.show()
