# Todo lo que se ponga en la clase padre se debe de poder usar en las clases hijas

# class Ave:
#     def volar(self):
#         return 'estoy volando'

# class Pinguino(Ave):
#     def volar(self):
#         return 'no puedo volar'
    
# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))

# Volvemos a estructurar para que se cumpla el principio!!!

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return 'Puedo volar'
    
class AveNoVoladora(Ave):
    pass