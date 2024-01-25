#El objeto es una instancia de una clase

class Persona:
    #__init__ es un metodo especial para inicializar los atributos
    def __init__(self, nombre, edad, genero):  #self hace referencia a instancia de clase
        self.nombre = nombre  #nombre, edad, genero son los atributos para esta clase
        self.edad = edad
        self.genero = genero
     
    # definir metodo    
    def mostar(self):
        print(f"Nombre: {self.nombre} , Edad: {self.edad} , Genero: {self.genero}")   
 
#crear una instancia de una clase es un objeto
persona = Persona("Robeto", 25, "Masculino")

#imprimir
print(persona.edad)
persona.mostar()        