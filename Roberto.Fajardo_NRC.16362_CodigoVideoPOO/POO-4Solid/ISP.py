from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comerdor(ABC):   
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):   
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comerdor, Durmiente):
    def comer(self):
        print("El humano esta comiendo")
    
    def trabajar(self):
        print("El humano esta trabajando")
    
    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador): 
    def trabajar(self):
        print("El robot esta trabajando")
        
robot = Robot()  
humano = Humano()
robot.trabajar() 
humano.trabajar()
humano.comer()
humano.dormir()