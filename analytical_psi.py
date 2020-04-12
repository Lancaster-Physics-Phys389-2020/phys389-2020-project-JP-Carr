
from math import sin,pi
import matplotlib.pyplot as plt
import numpy as np
from probability_plotter import normalise

length=1
def psi(x_array,n,L):
    psi=np.array([sin((x+length/2)*pi*n/L) for x in x_array]) #accounts for not starting at x=0
    return psi*normalise(psi, x_array)

if __name__=="__main":
    plt.figure("Analytical Wavefunctions")
    for n in range(1,11):
    
        x=np.linspace(-length/2,length/2,1000)
        y=psi(x,n,length)
        plt.plot(x,y,label="n="+str(n))
        plt.legend()
    plt.show()