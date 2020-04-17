#from sympy import symbols
import numpy as np
    
        
class potential:
    def __init__(self,steps,form="SW"):
        """
        Initialises potential field and generates potential array

        Parameters
        ----------
        steps : int
            Number of integration points used in the calculation of wavefunction ψ.
        form : str, optional
            Describes the shape of the potential. The default is "SW".

        Returns
        -------
        None.

        """
        self.form=form
        self.steps=steps
        
        if self.form=="SW":
            self.V=np.array([1 for i in range(steps)])
   
        
    def V_depth(self):
        """
        Finds the depth of the potential well from the potential array

        Returns
        -------
        min_V : float
            The minimum potential value.

        """
        depth=-np.max(self.V)
        return depth
    
    def nu(self):
        """
        Calculates nondimensionalised potential nu

        Returns
        -------
        nu_array : numpy.ndarray
            An array of nondimensionalised potential.

        """
        nu_array=self.V/self.V_depth()
        return nu_array
        

