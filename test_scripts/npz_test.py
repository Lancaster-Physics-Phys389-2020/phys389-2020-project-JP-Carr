import numpy as np

a=np.array([1,2,3])
b=np.array([9,8,7])

np.savez("test.npz",x=a,y=b)

data=np.load("test.npz")
print(data["x"])
print(data["y"])