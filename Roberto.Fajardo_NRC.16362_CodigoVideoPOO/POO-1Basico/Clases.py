#Clases : Son una plantilla para definir metodos y atributos

#clase de sentencia nula
class Animal:
    pass

#Clase con parametros estaticos para cuando se la intancia
class Moto():
    #marca actua como variale = "Daytona" es la deficion de la variable
    marca = "Daytona" 
    modelo = "Txz"
    cilindraje = "125cc"

#clase con valores para asisgnarles    
class Persona:
    #__init__ es un metodo especial para inicializar los atributos
    def __init__(self, nombre, edad, genero):  #self hace referencia a instancia de clase
        self.nombre = nombre  #nombre, edad, genero son los atributos para esta clase
        self.edad = edad
        self.genero = genero
     
    #metodo    
    def mostar(self):
        pass    
            