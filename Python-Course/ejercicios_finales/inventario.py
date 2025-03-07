'''
Simulador de Inventario (POO + Listas + Diccionarios)
Descripción:
Simula un inventario de productos de una tienda.

Requisitos:  
- Crea una clase `Producto` con atributos como `nombre`, `precio` y `cantidad`.
- Usa un diccionario para almacenar los productos.
- Permite agregar productos, actualizar cantidades y generar un informe.
'''

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre 
        self.precio = precio
        self.cantidad = cantidad
        
        