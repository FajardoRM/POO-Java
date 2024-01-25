def decorador(funcion):
    def funcionModificada():
        print("Primer llamado de la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcionModificada

@decorador
def saludo():
    print("Hola como estas")
    
saludo()        