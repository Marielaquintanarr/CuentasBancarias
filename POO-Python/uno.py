# Juego uno
# azul, verde, amarillo, rojo
# 1 - 9
# jugadores
# cartas especiales "Salto", "Reversa", 
# "+2", "+4", y "Cambio de color"
# numero de jugadores * 7 
# En su turno, un jugador debe jugar una carta del
# mismo color o número que la última carta en la pila.
# Si no puede jugar, debe robar una carta del mazo.

class Jugador:
    def __init__(self, nombre, num_jugador):
        self.nombre = nombre
        self.num_jugador = num_jugador
        self.cartas = []

    def obtener_ultima_carta(self):
        return self.cartas[-1]
    
    def agregar_cartas(self, carta):
        self.cartas.append(carta)

    def mostrar_cartas(self):
        for carta in self.cartas:
            print(carta)

    def dejar_carta(self, ultima_carta):
        # dejar cartas
        # si es del mismo color o numero, si es un comodin
        # for i, carta in enumerate(self.cartas):
        #     if carta.color == ultima_carta.color or carta.simbolo in ['Cambio de color', '+4']:
        #         # agregar a la baraja
        #         baraja.append(i)
        for i, carta in enumerate(self.cartas):
            return self.cartas.pop(i)

     
class Carta:
    def __init__(self, color, simbolo):
        self.color = color
        self.simbolo = simbolo
    
    def __str__(self):
        return f'{self.simbolo} {self.color}'
    
# la baraja tiene 56 - 8 jugadores max
colores = ["rojo", "azul", "verde", "amarillo"]
valores = [str(i) for i in range(10)] + ["Salto", "Reversa", "+2"]
especiales = ["+4", "Cambio de color"]

# Crear baraja
baraja = [Carta(color, valor) for color in colores for valor in valores] * 2
baraja += [Carta("especial", esp) for esp in especiales] * 4

# for carta in baraja:
#     print(carta)

mariela = Jugador('mariela', 1)
anapau = Jugador('anapau', 2)
camila = Jugador('camila', 3)

jugadores = []
jugadores.append(mariela)
jugadores.append(anapau)
jugadores.append(camila)

# repartir de a 7 cartas para empezar
if len(baraja) >= (7 * len(jugadores)):  
    for jugador in jugadores:  
        for _ in range(7):  
            jugador.agregar_cartas(baraja.pop())  

# juego 
# mientras ninguno se quede sincartas
for jugador in jugadores:
    ultima_carta = jugador.obtener_ultima_carta()
    carta = baraja[-1]

    if carta.color == ultima_carta.color or carta.simbolo == ultima_carta.simbolo  or ultima_carta.simbolo in ['Cambio de color', '+4']:
        jugador.dejar_carta(ultima_carta)
        baraja.append(ultima_carta)
        jugador.mostrar_cartas()
    else:
        while carta.color != ultima_carta.color or carta.simbolo != ultima_carta.simbolo  or ultima_carta.simbolo not in ['Cambio de color', '+4']:
            jugador.agregar_cartas(baraja[-1])


