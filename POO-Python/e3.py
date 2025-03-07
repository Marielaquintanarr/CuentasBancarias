# crear plantilla

class Personaje():
    def __init__(self, nombre, habilidad, poder):
        self.nombre = nombre
        self.habilidad = habilidad
        self.poder = poder
    
    def __add__(self, otro_poder):
        nuevo_poder = ((self.poder + otro_poder.poder) // 2) ** 2
        return Personaje('Se ha creado un nuevo jugador con poder: ', ((self.poder + otro_poder.poder) // 2) ** 2, nuevo_poder)    


class Villano(Personaje):
    def __init__(self, nombre, habilidad, poder, nivel_maldad):
        super().__init__(nombre, habilidad, poder)
        self.nivel_maldad = nivel_maldad

    def presentarse(self):
        print(f'Soy {self.nombre}, mi habilidad es {self.habilidad}, tengo {self.poder} nivel de poder y soy {self.nivel_maldad}')

class Heroe(Personaje):
    def __init__(self, nombre, habilidad, poder, nivel_bondad):
        super().__init__(nombre, habilidad, poder)
        self.nivel_bondad = nivel_bondad   

    def presentarse(self):
        print(f'Soy {self.nombre}, mi habilidad es {self.habilidad}, tengo {self.poder} nivel de poder y soy {self.nivel_bondad}')


heroe = Heroe('Mariela', 'Desaparecer', 500, 'Buena')
villano = Heroe('Jaime', 'Ser malo', 50, 'Malo')   

heroe.presentarse()
villano.presentarse()

r = heroe + villano 
print(r.poder)