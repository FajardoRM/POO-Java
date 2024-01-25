class Animal:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        
    def alimentar(self):
        print("Estoy alimentandome")   
    
class Mascota(Animal):
    def __init__(self, nombre, edad, especie, color, peso):
        super().__init__(nombre, edad, especie) 
        self.color = color
        self.peso = peso
        
mascota = Mascota("Firulay", 7, "Mamifero", "negro", "35kg")   

print(mascota.nombre)  
mascota.alimentar()      