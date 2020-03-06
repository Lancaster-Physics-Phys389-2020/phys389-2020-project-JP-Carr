from sympy import symbols
import numpy as np
"""
class potential:
    def __init__(self,lower_limit,upper_limit,form="ISW",k=1):
        self.form=form
        self.k=k
        self.lower_limit=lower_limit #points at which V(x)=∞
        self.upper_limit=upper_limit
        
        if self.form=="ISW":
            return np.array([-1 for i in range])
            
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
        
class potential:
    def __init__(self,steps,form="ISW"):
        """
        Initialises potential field and generates potential array

        Parameters
        ----------
        steps : int
            Number of integration points used in the calculation of wavefunction.
        form : str, optional
            Describes the shape of the potential. The default is "ISW".

        Returns
        -------
        None.

        """
        self.form=form
        self.steps=steps
        
        if self.form=="ISW":
            self.V=np.array([-1 for i in range(steps)])
   
        
    def V_min(self):
        """
        Finds the minimum value in the potential array

        Returns
        -------
        min_V : float
            The minimum potential value.

        """
        min_V=np.min(self.V)
        return min_V
    
    def nu(self):
        """
        Calculates nondimensionalised potential nu

        Returns
        -------
        nu_array : numpy.ndarray
            An array of nondimensionalised potential.

        """
        nu_array=self.V/self.V_min()
        return nu_array
        
        
"""
x=potential(-1,1)

print(x.V(-1))
"""
