from numerov_s import numerov
from scipy import constants as const
import numpy as np

initial_conditions=(0,1E-10) #(ψ₁,ψ₂)
L=1 #length of potential V(x)≠0
integration_step=L/1000
step_num=round(1/L) #number of steps taken during integration
tolerance=1E-10 #maximum error on ψ(L)=0
wavefunction=[i for i in initial_conditions] #records the 
energy_levels=[]

def potential(k=1):
    x_list=np.linspace(0,L,step_num)
    return 0.5*k*x_list**2

print potential
#numerov(initial_conditions[0],initial_conditions[1],1,integration_step,)