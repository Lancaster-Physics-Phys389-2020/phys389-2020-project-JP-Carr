import numpy as np
import matplotlib.pyplot as plt
from os import listdir
import pandas as pd



wave_function_csv=listdir("wavefunctions")[0]  #temporary
#print(str(wave_function_csv))
data=pd.read_csv("wavefunctions\\"+str(wave_function_csv))
N=len(data)

x_array=np.linspace(-1/2,1/2,N)


plt.figure("Wavefunctions (N={})".format(N))
    
plt.xlabel("x")
plt.ylabel("P(x)")
  
i=1 
while 1:
    try:
        prob=data[str(i)]**2
        integral=np.trapz(prob,x=x_array)
        prob_norm=prob/integral
        print(np.trapz(prob_norm,x=x_array))
        
        plt.plot(x_array,prob_norm, label="n="+str(i))
        i+=1
    except:
        break
    
plt.tick_params(which='both',direction='in',right=True,top=True)
plt.legend()
plt.show()