from equation_parent import equation
from scipy import constants as const

class numerov(equation):
    """
    Numerical solution to time-independant Schrödinger equation for a quantum harmonic oscillator
    Derivation at http://www.fisica.uniud.it/~giannozz/Corsi/MQ/LectureNotes/mq.pdf
    """
    def __init__(self,y0,y1,n,E,V,delta_x,name="Numerov’s formula"):
        super().__init__(name)
        self.E=E #Energy
        self.V=V #Potential
        self.delta_x=delta_x
        self.y0=y0 #y_(n-1)  - first value of ψ in intergration
        self.y1=y1 #y_n
        self.n=n
        
    def g_n(self,n=None):
        return (2*const.m_e/const.hbar**2)*(self.E-self.V)
   
    def f_n(self,n):
        return 1+self.g_n(n)*(self.delta_x**2/12)
    
    def __call__(self):
        return ((12-10*self.f_n(self.n)) * self.y1-  self.f_n(self.n-1) * self.y0)    /self.f_n(self.n)
    

#x=numerov(0, 1E-10, 0,1,0,2000)
        
#print(x)
        
#print(numerov(0, 1E-10, 0,1,0,2000))
