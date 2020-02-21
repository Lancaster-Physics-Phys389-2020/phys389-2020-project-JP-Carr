from abc import abstractmethod
class equation:
    """
    Parent class for all equation classes
    """
    def __init__(self,name):
        self.name=name
        
    @abstractmethod
    def __call__(self):
        pass
    
    def __repr__(self):
        return self.name+" = "+str(self.__call__())

"""
class add(equation):
    
    def __init__(self,name):
        super().__init__(name)
    def __call__(self):
        return self.i
    
    
x=add("2+2",4)

print(x)
"""