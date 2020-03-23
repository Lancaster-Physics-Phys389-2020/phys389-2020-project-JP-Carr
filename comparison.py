import pandas as pd
from analytical_E_levels import analytical_E

df=pd.read_csv("energy_levels.csv")
x=[[df["n"][i],df["epsilon"][i]] for i in range(len(df["n"]))] #maybe a dictionary?
for i in x:
    print (i)