'''
Juego de Cartas
Objetivo: Practicar polimorfismo y diseño de sistemas.
Descripción:
Crea una clase Carta con atributos como palo y valor.
Diseña una clase Baraja que contenga todas las cartas posibles y 
permita mezclarlas.
Agrega una clase abstracta JuegoDeCartas con métodos como iniciar_juego.
Implementa juegos concretos como Poker o Blackjack.
'''

class Jugador:
    def __init__(self, nombre, apuesta):
        self.nombre = nombre
        self.cartas = []
        self.apuesta = apuesta

    def intercambiar_carta(self, carta):
        # cambiar una carta de la baraja del jugador por una carta de la baraja de la casa
        pass

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def aumentar_apuesta(self, nuevo_valor):
        self.apuesta = nuevo_valor
    
    def salir_del_juego(self):
        # eliminar el objeto del jugador e imprimir el jugador ha salido del juego
        print(f'El jugador {self.nombre} ha salido del juego.')

    def imprimir_cartas(self):
        print(f'Cartas de {self.nombre}')
        for carta in self.cartas:
            print(carta)

    
class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
    
    def __str__(self):
        return f'{self.palo} de {self.valor}'



from random import shuffle
class Baraja:
    def __init__(self):
        self.cartas = []
        
    def agregar_carta(self, palo, valor):
        carta = Carta(palo, valor)
        self.cartas.append(carta)
    
    def barajear_cartas(self):
        shuffle(self.cartas)
        return self.cartas
    
    def repartir_cartas(self, jugador, cantidad):
        if len(self.cartas) >= cantidad:
            for _ in range(cantidad):
                carta = self.cartas.pop()  
                jugador.agregar_carta(carta)
        else:
            print("No hay suficientes cartas para repartir.")

    def imprimir_cartas(self):
        for carta in self.cartas:
            print(carta)



# jugador
# tiene que recibir 5 cartas
# tiene una apuesta
# se hace ronda de apuestas
# se revelan 3 cartas de la baraja
# segunda ronda de apuestas
# se revela la cuarta carta
# tercera ronda de apuestas
# se revela la quinta carta
# ultima ronda de apuestas




# crear objetos
mariela = Jugador('Mariela', 2000)
jimmy = Jugador('Jimmy', 2000)
casa = Jugador('Casa', 0)

baraja = Baraja()
for n in range(2, 11):
    baraja.agregar_carta(n, 'treboles')

for n in range(2, 11):
    baraja.agregar_carta(n, 'corazones')

for n in range(2, 11):
    baraja.agregar_carta(n, 'diamantes')

for n in range(2, 11):
    baraja.agregar_carta(n, 'espadas')

baraja.agregar_carta('A', 'corazones')
baraja.agregar_carta('A', 'treboles')
baraja.agregar_carta('A', 'diamantes')
baraja.agregar_carta('A', 'espadas')

baraja.agregar_carta('J', 'corazones')
baraja.agregar_carta('J', 'treboles')
baraja.agregar_carta('J', 'diamantes')
baraja.agregar_carta('J', 'espadas')


baraja.agregar_carta('Q', 'corazones')
baraja.agregar_carta('Q', 'treboles')
baraja.agregar_carta('Q', 'diamantes')
baraja.agregar_carta('Q', 'espadas')


baraja.agregar_carta('K', 'corazones')
baraja.agregar_carta('K', 'treboles')
baraja.agregar_carta('K', 'diamantes')
baraja.agregar_carta('K', 'espadas')


# baraja.imprimir_cartas()
# baraja.barajear_cartas()
# print('barajeadas')
# baraja.imprimir_cartas()

# ya que se creo la baraja se reparten las cartas entre cada jugador
# Repartir 5 cartas
print('')
baraja.repartir_cartas(mariela, 5)
baraja.repartir_cartas(jimmy, 5)
baraja.repartir_cartas(casa, 5)
# Imprimir cartas de cada jugador
mariela.imprimir_cartas()
print('')
jimmy.imprimir_cartas()
print('')
casa.imprimir_cartas()