import numpy as np    
from error import error
        
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
        else:
            error("The form \"{}\" is not currently defined".format(self.form))
   
        
    def V_depth(self):
        """
        Finds the depth of the potential well from the potential array

        Returns
        -------
        depth : float
            The depth of the potential well.

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
        

