

# # diseñar para reutilizar
# # que el codigo sea legible (claro y limpio)
# # extensible, el software debe de poder extenderse sin que lo downgradee

# # Principio 1: SRP
# # Principio de responsabilidad unica (cada clase solo debe de tener una tarea)

# class Auto:
#     def __init__(self):
#         self.posicion = 0
#         self.combustible = 100

#     def mover(self, distancia):
#         if self.combustible >= distancia / 2:
#             self.posicion += distancia
#             self.combustible -= distancia / 2
#         else:
#             print('Hace falta combustible')
    
#     def cargar_gasolina(self, cantidad):
#         self.combustible += cantidad
    
#     def obtener_combustible(self):
#         return self.combustible
    
# # ensto esta mal porque la clase se esta encargando del movimiento de un auto y aparte del combustible



class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print('Has movido el auto')
        else:
            print('Hace falta combustible')

    def obtener_posicion(self):
        return self.posicion
    
class TanquedeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


tanque = TanquedeCombustible()
auto = Auto(tanque)
print(auto.obtener_posicion())
print(auto.mover(10))
print(auto.obtener_posicion())
