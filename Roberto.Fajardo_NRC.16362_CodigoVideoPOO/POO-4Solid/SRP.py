class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtenerCombustible() >= distancia /2:
            self.posicion += distancia
            self.tanque.usarCombustible(distancia /2)
            return("haz movido el auto exitosamente")     
        else:
            return("No hay  suficiente combustible")

    def obtenerPosicion(self):
        return self.posicion        

class TanqueDeCombustible:
    def __init__(self):
        self.combustible=100  
    
    def agregarCombustible(self, cantidad):
        self.combustible += cantidad 

    def obtenerCombustible(self):
        return self.combustible

    def usarCombustible(self, cantidad):
        self.combustible -= cantidad              

tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtenerPosicion())
print(autito.mover(10))
print(autito.obtenerPosicion())
print(autito.mover(20))
print(autito.obtenerPosicion())
print(autito.mover(60))
print(autito.obtenerPosicion())
print(autito.mover(100))
print(autito.obtenerPosicion())
print(autito.mover(100))