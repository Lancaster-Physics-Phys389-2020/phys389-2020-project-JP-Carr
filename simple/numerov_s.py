from scipy import constants as const

    def g_n(n,V):
        return (2*const.m_e/const.hbar**2)*(E-V)
   
    def f_n(n,V):
        return 1+g_n(n,V)*(delta_x**2/12)
    
    def numerov(y0,y1,V,E,x,delta_x):#n start at 1
        
        
        
        return ((12-10*f_n(n,V)) * y1-  f_n(n-1,V) * y0)    /f_n(n,V)