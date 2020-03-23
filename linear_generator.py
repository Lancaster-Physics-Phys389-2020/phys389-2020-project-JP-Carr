import wavefunction_generator as mfg
import time

start=time.time()

for i in range(1,3):
    mfg.run(i)

print("Time elapsed = {}s".format(round(time.time()-start,2)))