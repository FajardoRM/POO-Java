class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar(self):
        print(f"Nombre:  {self.nombre} , Eda: {self.edad}")
        
class Docente(Persona):
    def __init__(self, nombre, edad, masetria):
        super().__init__(nombre, edad)
        self.masetria = masetria
    
    def mostraMaestria(self):
        print("Mi maestria es en: ")
        
docente = Docente("Manuel", 34, "Informatica")

docente.mostrar()
docente.mostraMaestria()                      