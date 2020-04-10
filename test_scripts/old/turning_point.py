#TURNING POINT TEST

import numpy as np
import matplotlib.pyplot as plt

y=np.array([1,2,3,1,2,3,1,2,3,1,2,3]) #6 turning points

def turn_points(array):
    n=0
    for i in range(1,len(array)-1):
        if (array[i]<array[i-1] and array[i]<array[i+1]) or (array[i]>array[i-1] and array[i]>array[i+1]):
            n+=1
    return n
            
x=np.linspace(0,len(y),len(y))            
plt.plot(x,y)
print(turn_points(y))