import wavefunction_generator as wfg
import multiprocessing as mp
import time

start=time.time()
simulations = 8 #Number of simulations to run (NOTE: Each successive simulation takes longer to run)


if __name__ == "__main__":  # Allows for the safe importing of the main module
    print("There are {} logical processors on this machine".format(mp.cpu_count()))
    print("Running {} simulations...".format(simulations))
    
    max_processes = mp.cpu_count()
    pool = mp.Pool(max_processes)
    processes = pool.map_async(wfg.run, range(1,simulations+1))
    pool.close()
    pool.join()

    print("Time elapsed = {}s".format(round(time.time()-start,2)))
    print("\a")