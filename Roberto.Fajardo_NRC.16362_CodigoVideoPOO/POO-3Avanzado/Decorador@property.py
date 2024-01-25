class Alumno:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property   #para getter
    def nombre(self):
            return self._nombre
        
    @nombre.setter   #para setter
    def nombre(self, new_nombre):
            self._nombre = new_nombre  
    
    @property   #para getter
    def edad(self):
            return self._edad
        
    @edad.setter   #para setter
    def edad(self, new_edad):
            self._edad = new_edad        
            
alumno = Alumno("Pedro", 18) 

nombre = alumno.nombre    
print(nombre)  

alumno.edad = 25
edad = alumno.edad
print(edad)     