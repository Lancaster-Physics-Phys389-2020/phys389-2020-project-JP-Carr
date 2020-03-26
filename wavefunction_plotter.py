import numpy as np
import matplotlib.pyplot as plt
from os import listdir
import pandas as pd



wave_function_csv=listdir("wavefunctions")[0]  #temporary
data=pd.read_csv("wavefunctions\\"+str(wave_function_csv))
N=len(data)

x_array=np.linspace(-1/2,1/2,N)


plt.figure("Wavefunctions (N={})".format(N))
    
plt.xlabel("x")
plt.ylabel("ψ")
  
i=1 
while 1:
    try:
        plt.plot(x_array,data[str(i)], label="n="+str(i))
        i+=1
    except:
        break
    
    
plt.legend()
plt.show()