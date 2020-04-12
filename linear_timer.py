from wavefunction_generator import run
import numpy as np
store=[[],[]]
for i in range(1,31):
    N,t=run(i)
    print(N,t)
    store[0].append(N)
    store[0].append(t)
    
out=np.array(store)
np.save("linear_time.npy",out)
print("\a")