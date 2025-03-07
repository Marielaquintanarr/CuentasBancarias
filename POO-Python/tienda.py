'''
7. Simulador de Tienda
Objetivo: Practicar abstracción, herencia y 
encapsulación.
Descripción:
Crea una clase Producto con atributos como nombre, 
precio, y stock.
Diseña una clase CarritoDeCompras para añadir productos, eliminar 
productos, y calcular el total.
Implementa métodos para aplicar descuentos y mostrar el resumen del carrito.
'''
from abc import ABC, abstractmethod

class Producto:
    def __init__(self, nombre, precio, stock, descuento):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.descuento = descuento
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def precio(self):
        return self.__precio
    @property
    def stock(self):
        return self.__stock
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    @precio.setter
    def precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    @stock.setter
    def stock(self, nuevo_stock):
        self.stock = nuevo_stock
    
    def aplicar_descuento(self):
        total_descuento = self.precio - ((self.precio * self.descuento) / 100)
        print(f'El producto {self.nombre} cuesta: {total_descuento} despues de su descuento.')
    
    def __str__(self):
        return f'{self.nombre}, {self.precio}, {self.stock}, {self.descuento}'

# Implementa métodos para aplicar descuentos y mostrar 
# el resumen del carrito.
class CarritoDeCompras:
    #añadir productos, eliminar productos, y calcular el total.
    def __init__(self):
        self.carrito = []
        self.total = 0
    
    def mostrar_productos_del_carrrito(self):
        for product in self.carrito:
            print(product)

    def agregar_productos(self, nombre, precio, stock, descuento):
        producto = Producto(nombre, precio, stock, descuento)
        self.carrito.append(producto)
    
    def mostrar_total_con_decuento(self):
        for producto in self.carrito:
            total_descuento = producto.precio - ((producto.precio * producto.descuento) / 100)
            print(f'Total con descuento: {total_descuento}')

    def mostrar_total(self):
        for producto in self.carrito:
            self.total += producto.precio
        print(f'El total es: {self.total}')
    
    def eliminar_producto(self, nombre_producto):
        for i, producto in enumerate(self.carrito):
            if producto.nombre == nombre_producto:
                del self.carrito[i]
                print(f'El producto {producto.nombre} ha sido eliminado del carrito')

pasta = Producto('Pasta Colgate', 20.0, 50, 12)
chips = Producto('Chips Fuego', 65.50, 20, 5)
jabon = Producto('Jabón Acción', 35.80, 30, 15)

carrito = CarritoDeCompras()
carrito.agregar_productos('Pasta Colgate', 20.0, 50, 12)
carrito.agregar_productos('Chips Fuego', 65.50, 20, 10)
carrito.agregar_productos('Jabón Acción', 35.80, 30, 15)

carrito.mostrar_total()
carrito.mostrar_total_con_decuento()
carrito.eliminar_producto('Pasta Colgate')
print('')
print('despues')
carrito.mostrar_total()
carrito.mostrar_total_con_decuento()
carrito.mostrar_productos_del_carrrito()