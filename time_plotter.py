import numpy as np
import matplotlib.pyplot as plt 
from error import error

"""
Plots process timing data produced by "linear_timer.py"
"""
path="linear_time.npy"

try:
    file=np.load(path,allow_pickle=True)[0]
except:
    error("Unable to load \"{}\" ".format(path))
    
    

N=[file[2*i] for i in range(int((len(file)-1)/2))]    # sorting data into two separate lists for plotting
t=[file[2*i+1] for i in range(int((len(file)-1)/2))]
print(N)
plt.figure("Processing time")
plt.xlabel("N")
plt.ylabel("Time (s)")
plt.tick_params(which='both',direction='in',right=True,top=True)
plt.plot(N,t)
plt.show()