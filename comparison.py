import pandas as pd
from analytical_E_levels import analytical_E
import matplotlib.pyplot as plt
from os import listdir
from error import error
import numpy as np
import math

all_csvs=listdir("energy_levels")
for i in all_csvs:  #filters out non-csv files/directories 
    if ".csv" not in i:
        all_csvs.remove(i)
#print(all_csvs)
try:
    dfs=[pd.read_csv("energy_levels\\"+ file) for file in all_csvs]
except:
    error("Unable to read 1 or more CSVs")
dic={}
for df in dfs:    
    dic[str(df.columns[0])]=[[df["n"][i],df["epsilon"][i]] for i in range(len(df["n"]))]
  #  print (dic[str(df.columns[0])])
  #  print("\n")

max_dif=[]
plt.figure("comparison") #rename
for i in dic:
  #  print(i)
 #   print(dic[i])
    #print("\n")
    x=np.array([j[0] for j in dic[i]])
    numerical_epsilon=np.array([j[1] for j in dic[i]])
    analytical_epsilon=analytical_E(x)
    y=numerical_epsilon/-analytical_epsilon
    
   # print(y)

    plt.plot(x,y, label="N="+i)
    
    
    max_dif.append([int(i),max([abs(max(y)-1),abs(min(y)-1)])])
   # print(type(i))
   # print(type(max([abs(max(y)-1),abs(min(y)-1)])))
  #  max_dif[1].append(max([abs(max(y)-1),abs(min(y)-1)]))
   # print(i,max([abs(max(y)-1),abs(min(y)-1)]))
plt.xlabel("n")
plt.ylabel(r"$\epsilon_{numerical}/\epsilon_{analytical}$")
plt.tick_params(which='both',direction='in',right=True,top=True)
plt.legend()

plt.figure("Maximum difference")
plt.xlabel("N")
plt.ylabel(r"$log(\Delta \epsilon_{max})$")
plt.tick_params(which='both',direction='in',right=True,top=True)
dif_x=np.array([i[0] for i in sorted(max_dif)])
dif_y=np.array([math.log10(i[1]) for i in sorted(max_dif)])
plt.plot(dif_x,dif_y,"r+")

plt.show()

print(max(dif_y))