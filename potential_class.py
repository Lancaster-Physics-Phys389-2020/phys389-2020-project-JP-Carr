from sympy import symbols

class potential:
    def __init__(self,lower_limit,upper_limit,form="harmonic",k=1):
        self.form=form
        self.k=k
        self.lower_limit=lower_limit #points at which V(x)=∞
        self.upper_limit=upper_limit
            
    def V(self,position):
      #  print(position)
        infinity_approximation=1E100
        x=symbols('x')
        if self.form=="harmonic":            
            V=0.5*self.k*x**2
        if self.form=="ISW": #infinte square well   
            V=0*x
        
        if position<=self.lower_limit or position>=self.upper_limit:
         #   print("∞ {}".format(position))
            return V.subs(x,position)#infinity_approximation
        else:
           # print("finite potential")
            return V.subs(x,position)
        
        
"""
x=potential(-1,1)

print(x.V(-1))
"""
