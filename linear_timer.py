from wavefunction_generator import run
import numpy as np
"""
Times "wavefunction_generator.py" at different values of N
"""
simulations=10 # number of simulations to be run (NOTE: this can take a long time for a large number of simulations

store=[[],[]]
for i in range(1,simulations+1):
    N,t=run(i)
    print(N,t)
    store[0].append(N)
    store[0].append(t)
    
out=np.array(store)
np.save("linear_time.npy",out)
print("\a")