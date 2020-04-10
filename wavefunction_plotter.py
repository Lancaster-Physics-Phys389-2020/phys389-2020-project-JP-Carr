import numpy as np
import matplotlib.pyplot as plt
from os import listdir
import pandas as pd
from error import error




#print(wave_function_csv)
try:
    wave_function_csv="wavefunctions_N=1000.csv"#listdir("wavefunctions")[0]  #temporary
    
except:
    error("Unable to load"+str(wave_function_csv))
data=pd.read_csv("wavefunctions\\"+str(wave_function_csv))
N=len(data)

x_array=np.linspace(-1/2,1/2,N)


plt.figure("Wavefunctions (N={})".format(N))
    
plt.xlabel(r"$\tilde{x}$")
plt.ylabel(r"$\psi\tilde{x}$")
  
i=1 
while 1:
    try:
        plt.plot(x_array,data[str(i)], label="n="+str(i))
        i+=1
    except:
        break
    
plt.tick_params(which='both',direction='in',right=True,top=True)
plt.legend()
plt.show()