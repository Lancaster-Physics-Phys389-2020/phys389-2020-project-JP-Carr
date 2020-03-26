import pandas as pd
from analytical_E_levels import analytical_E
import matplotlib.pyplot as plt
from os import listdir
from error import error
import numpy as np

all_csvs=listdir("energy_levels")
print(all_csvs)
try:
    dfs=[pd.read_csv("energy_levels\\"+ file) for file in all_csvs]
except:
    error("Unable to read 1 or more CSVs")
dic={}
for df in dfs:    
    dic[str(df.columns[0])]=[[df["n"][i],df["epsilon"][i]] for i in range(len(df["n"]))]
  #  print (dic[str(df.columns[0])])
  #  print("\n")
    
plt.figure("comparison") #rename
for i in dic:
  #  print(i)
 #   print(dic[i])
    print("\n")
    x=np.array([j[0] for j in dic[i]])
    numerical_epsilon=np.array([j[1] for j in dic[i]])
    analytical_epsilon=analytical_E(x)
    y=numerical_epsilon/-analytical_epsilon
    
   # print(y)
    
    
    
    
    
    plt.plot(x,y, label="N="+i)
    plt.xlabel("n")
    plt.ylabel(r"$\epsilon_{numerical}/\epsilon_{analytical}$")
    #plt.ylabel(r"$\frac{\epsilon_{numerical}}{\epsilon_{analytical}}$")
    plt.legend()
    plt.show()
    """
    for j in dic[i]:
        print(j[1],j[0])
        plt.plot(j[1],j[0])
    plt.show()
    """