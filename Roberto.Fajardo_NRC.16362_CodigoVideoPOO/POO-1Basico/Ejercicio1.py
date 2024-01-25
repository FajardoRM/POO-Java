class Docente:
    def __init__(self, nombre, edad, maestria):
        self.nombre = nombre
        self.edad = edad
        self.maestria = maestria
        
    def enseniar(self):
        print("Enseñando...")
        
nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
maestria = input("Digite su maetria: ")

docente = Docente(nombre, edad, maestria)

print(f"""IMPRESION DATOS
      nombre: {docente.nombre}
      Edad: {docente.edad}
      Maestria: {docente.maestria}
      """)

while True:
    enseniar = input()
    if(enseniar.lower()== "enseñar" ):
        docente.enseniar() 