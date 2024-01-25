from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificarPalabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificarPalabra(self, palabra):
        if palabra.lower() in ["hola", "adios", "python"]:
            return True
        else:
            return False

class ServicioOnline:
    def __init__(self, verificador):
        self.verificador = verificador

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregirTexto(self, texto):
        palabras = texto.split()
        correcciones = []
        for palabra in palabras:
            if not self.verificador.verificarPalabra(palabra):
                correcciones.append(f"Corregir: {palabra}")
            else:
                correcciones.append(palabra)
        return ' '.join(correcciones)

# Crear instancias
diccionario = Diccionario()
servicio_online = ServicioOnline(diccionario)
corrector = CorrectorOrtografico(diccionario)

# Uso del corrector ortográfico
texto_a_corregir = "Hola, este es un ejamplo de texo con errores."
texto_corregido = corrector.corregirTexto(texto_a_corregir)
print(f"Texto original: {texto_a_corregir}")
print(f"Texto corregido: {texto_corregido}")
