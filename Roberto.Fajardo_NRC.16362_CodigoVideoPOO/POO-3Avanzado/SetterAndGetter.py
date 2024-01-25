#set establecer
#get mostar

class Animal:
    def __init__(self, nombre, edad, especie):
        self._nombre = nombre
        self._edad = edad
        self._especie = especie
        
     #Getter and Setter para nombre   
    def get_nombre(self):
        return self._nombre  
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre 
     
    #Getter and Setter para edad       
    def get_edad(self):
        return self._edad  
    
    def set_edad(self, new_edad):
        self._edad = new_edad 
      
    #Getter and Setter para especie    
    def get_especie(self):
        return self._especie 
    
    def set_especie(self, new_especie):
        self._especie = new_especie  
        
animal = Animal("Firulay", 8, "Mamifero")        

nombre = animal.get_nombre()
print(nombre)  

animal.set_edad(12)
edad = animal.get_edad()
print(edad)    