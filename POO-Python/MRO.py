# Si esta super, llama al MRO

class A:
    def hablar(self):
        print('Hola desde A')

class B(A):
    def hablar(self):
        print('Hola desde B')

class C(A):
    def hablar(self):
        print('Hola desde C')

class D(C, B):
    pass
    # def hablar(self):
    #     print('Hola desde D')

# Aunque este heredando de otras clases se toma el metodo de la clase
d = D()
d.hablar()

# Si comento D, me devuelve B
# Si comento B me devuelve C
# si comento C me devuelve A

# Esto porque va por niveles

# Nivel 1:   A
# Nivel 2: B   C (la que este primero en la funcion)
# Nivel 3:   D

# es como un arbol, pasa por todo el arbol de un lado, si heredan de distintos

# Para saber esto de manera mas facil de que clase seguiria
print(D.mro())