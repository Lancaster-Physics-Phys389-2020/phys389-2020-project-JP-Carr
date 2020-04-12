import numpy as np
import matplotlib.pyplot as plt 

file=np.load("linear_time.npy",allow_pickle=True)[0]

N=[file[2*i] for i in range(int((len(file)-1)/2))]
t=[file[2*i+1] for i in range(int((len(file)-1)/2))]
print(N)
plt.figure("Processing time")
plt.xlabel("N")
plt.ylabel("Time (s)")
plt.tick_params(which='both',direction='in',right=True,top=True)
plt.plot(N,t)
plt.show()