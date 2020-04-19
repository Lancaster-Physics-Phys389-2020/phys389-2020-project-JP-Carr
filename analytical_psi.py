from math import sin,pi
import matplotlib.pyplot as plt
import numpy as np
from probability_plotter import normalise

length=1 #Length of potential well

def psi(x_array,n,L):
    """
    Produces a wavefunction of an infinite square potential well

    Parameters
    ----------
    x_array : numpy.ndarray
        Array of positional values.
    n : int
        Principle quantum number.
    L : float
        Length of potential well.

    Returns
    -------
    psi_norm : numpy.ndarray
        Normalised wavefunction.

    """
    psi=np.array([sin((x+length/2)*pi*n/L) for x in x_array]) #accounts for not starting at x=0
    psi_norm=psi*normalise(psi, x_array)    #normalises array
    return psi_norm

if __name__=="__main__":
    """
    Plots wavefunction if script is run directly
    """
    plt.figure("Analytical Wavefunctions")
    for n in range(1,11):
    
        x=np.linspace(-length/2,length/2,1000)
        y=psi(x,n,length)
        plt.plot(x,y,label="n="+str(n))
        plt.legend()
    plt.show()