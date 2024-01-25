from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, genero, actividad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.actividad = actividad 
        
    @abstractmethod
    def trabajar(self):
        pass 
    
    def presentar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

# 1     
class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, actividad):
        super().__init__(nombre, edad, genero, actividad)
        
    def trabajar(self):
        pass
    
    def hacerActividad(self):
        print(f"Estoy estudiando: {self.actividad}")

# 2      
class Docente(Persona):
    def __init__(self, nombre, edad, genero, actividad):
        super().__init__(nombre, edad, genero, actividad)
        
    def trabajar(self):
        pass
    
    def hacerActividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")        

estudiante1 = Estudiante("Manuel", 27, "Masculino", "Programación")    
docente = Docente("Rosa", 24, "femenino", "Pedagogia")  

estudiante1.presentar()
estudiante1.hacerActividad()
docente.presentar()
docente.hacerActividad()