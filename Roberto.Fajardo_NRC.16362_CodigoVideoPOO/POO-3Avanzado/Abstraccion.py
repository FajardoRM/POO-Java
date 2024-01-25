class Moto():
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendido"  
    
    def conducir(self):
        if self._estado == "apagado":
            self.encender()  
            print("Conducir la moto")  

moto = Moto()
moto.conducir()
         