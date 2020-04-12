import numpy as np
import matplotlib.pyplot as plt
from os import listdir
import pandas as pd
from error import error

def normalise(y_array,x_array):
    integral=np.trapz(y_array**2,x=x_array)
    const=1/integral
    return const**0.5

if __name__=="__main__":

    try:
        wave_function_csv="wavefunctions_N=1000.csv"#listdir("wavefunctions")[0]  #temporary
        
    except:
        error("Unable to load"+str(wave_function_csv))
    #print(str(wave_function_csv))
    data=pd.read_csv("wavefunctions\\"+str(wave_function_csv))
    N=len(data)
    
    position_array=np.linspace(-1/2,1/2,N)
    
    
    plt.figure("Probability (N={})".format(N))
        
    plt.xlabel(r"$\tilde{x}$")
    plt.ylabel(r"$|\psi(\tilde{x})|^2$")
    #plt.plot(x_array,normalise(data[str(1)]**2), label="n="+str(1)) 
    i=1 
    while 1:
        try:      
            prob=((normalise(data[str(i)],position_array))*data[str(i)])**2
            plt.plot(position_array,prob, label="n="+str(i))
            i+=1
        except:
            break
        
    plt.tick_params(which='both',direction='in',right=True,top=True)
    plt.legend()
    plt.show()
