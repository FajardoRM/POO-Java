#no existe con tal en python

class MiClase:
    def __init__(self):
        self._atributo = "Variable"  # atributo protegido
        self.__atributo = "Variable"  # atributo privado

    def _escuchar(self):  # método protegido
        print("¿Qué has escuchado?")

objeto = MiClase()
print(objeto._atributo)
objeto._escuchar()
          