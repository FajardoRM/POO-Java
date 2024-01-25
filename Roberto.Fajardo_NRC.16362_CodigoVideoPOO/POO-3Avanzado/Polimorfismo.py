class Pollo:
    def sonido(self):
        return "Pio Pio"
    
class Vaca:
    def sonido(self):
        return "Muu Muu"    
    
def hacerSonido(animal):
    print(animal.sonido())
    
pollo = Pollo()
vaca = Vaca()

hacerSonido(pollo)
print(vaca.sonido())        