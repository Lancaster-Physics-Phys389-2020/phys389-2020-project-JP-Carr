import pandas as pd
from analytical_E_levels import analytical_E
import matplotlib.pyplot as plt
from os import listdir
from error import error
import numpy as np
import math

all_csvs=listdir("energy_levels")
for i in all_csvs:  #filters out non-csv files/directories from "phys389-2020-project-JP-Carr\energy_levels"
    if ".csv" not in i:
        all_csvs.remove(i)

try:
    dfs=[pd.read_csv("energy_levels\\"+ file) for file in all_csvs] #create dataframe from E_n csv
except:
    error("Unable to read 1 or more CSVs")
dic={}  #dictionary to store relevent data from dataframe to allow for easy plotting
for df in dfs:    
    dic[str(df.columns[0])]=[[df["n"][i],df["epsilon"][i]] for i in range(len(df["n"]))]


max_dif=[]
plt.figure("comparison") #demonstrates the difference between the energy levels produced by different methods
for i in dic:

    x=np.array([j[0] for j in dic[i]])
    numerical_epsilon=np.array([j[1] for j in dic[i]])
    analytical_epsilon=analytical_E(x)
    y=numerical_epsilon/-analytical_epsilon
    plt.plot(x,y, label="N="+i)
    max_dif.append([int(i),max([abs(max(y)-1),abs(min(y)-1)])])  

plt.xlabel("n")
plt.ylabel(r"$\epsilon_{numerical}/\epsilon_{analytical}$")
plt.tick_params(which='both',direction='in',right=True,top=True)
plt.legend()

plt.figure("Maximum difference")  #plots the maximum difference between the two methods
plt.xlabel("N")
plt.ylabel(r"$log(\Delta \epsilon_{max})$")
plt.tick_params(which='both',direction='in',right=True,top=True)
dif_x=np.array([i[0] for i in sorted(max_dif)])
dif_y=np.array([math.log10(i[1]) for i in sorted(max_dif)])
plt.plot(dif_x,dif_y,"r+")

plt.show()

