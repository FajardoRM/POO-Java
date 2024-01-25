class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def presentarse(self):
        print("")   
    
class Conductor:
    def __init__(self, id):
        self.id = id
        
class Taxista(Persona, Conductor):
    def __init__(self, nombre, edad, genero, id,empresa, salario):
        Persona.__init__(self, nombre, edad, genero) 
        Conductor.__init__(self, id) 
        self.empresa = empresa
        self.salario = salario
        
    def presentarse(self):
        print(f"Hola soy {self.nombre} y trabajo en esta empresa: {self.empresa}") 
        
taxista = Taxista("Jose", 22, "Masculino", "12345678", "TaxDriv", 750)  

print(taxista.nombre)
print(taxista.id)
taxista.presentarse()         