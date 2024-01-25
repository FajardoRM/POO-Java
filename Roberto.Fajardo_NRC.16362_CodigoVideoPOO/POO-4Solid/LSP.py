class Ave:
    def __init__(self, nombre):
        self.nombre = nombre

class AveVoladora(Ave):
    def volar(self):
        return f"{self.nombre} está volando"

class AveNoVoladora(Ave):
    pass

#Instancias clases
ave_comun = Ave("Gorrión")
ave_voladora = AveVoladora("Águila")
ave_no_voladora = AveNoVoladora("Pingüino")

# Utilizar metodos
print(ave_voladora.volar())
print(f"{ave_comun.nombre} no puede volar.")
print(f"{ave_no_voladora.nombre} tampoco puede volar.")
