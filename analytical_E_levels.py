from scipy import constants as const

def analytical_E(n):
    gamma2=200
    return (n**2*const.pi**2)/gamma2 -1

#for n in range (1,11):
 #   print (analytical_E(n)) 