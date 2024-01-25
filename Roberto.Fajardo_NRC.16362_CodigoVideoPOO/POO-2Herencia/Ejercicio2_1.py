class Animal:
    def comer(self):
        print("Se esta alimentando")
    
class Hervivoro(Animal):
    def huir(self):
        print("Esta escapando")    
    
class Carnivoro(Animal):
    def cazar(self):
        print("Esta cazando") 
        
class Mascota(Hervivoro, Carnivoro):
    pass    

mascota = Mascota() 

mascota.comer()
mascota.huir()  
mascota.cazar()  