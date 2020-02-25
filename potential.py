from sympy import symbols

class potential:
    def __init__(self,lower_limit,upper_limit,form="harmonic",k=1):
        self.form=form
        self.k=k
        self.lower_limit=lower_limit #points at which V(x)=∞
        self.upper_limit=upper_limit
            
    def V(self,position):
        infinity_approximation=1E100
        x=symbols('x')
        if self.form=="harmonic":            
            V=0.5*self.k*x**2
        if self.form=="ISW": #infinte square well   
            V=0
        
        if x<=self.lower_limit or x>=self.upper_limit:
            return infinity_approximation
        else:
            return V.subs(x,position)
        
        
"""
x=potential()

print(x.V(12))
"""