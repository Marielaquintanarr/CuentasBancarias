# # dercoradores -> funciones especiales que decoran a otras
# # toma una funcion como entrada le agrega una funcionalidad extra y regresa la funcion modificada

# # sirven para validacion de entradas, excepciones


def decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar a la funcion')
        funcion()
        print('Despues de llamar a la funcion')
    return funcion_modificada()

# @decorador =
# def saludar():
#     print('Hola Mariela')
# saludo = decorador(saludar)

@decorador
def saludo():
    print('Hola')
saludo()
