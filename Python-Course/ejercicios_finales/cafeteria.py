import random as rd
from datetime import date


class Cliente:
    def generar_id(self):
        id = rd.randint(1, 1000)
        return id

    def __init__(self, nombre):
        self.id = self.generar_id()
        self.nombre = nombre
        self.pedidos = []
      
class Pedido:
    def generar_id(self):
        id = rd.randint(1, 1000)
        return id
    
    def __init__(self):
        #{producto, cantidad}
        self.id = self.generar_id()
        self.pedido = {}

    def agregar_producto(self, almacen, producto):
        # almacen.productos = {producto : cantidad}
        if producto in almacen.productos and almacen.productos[producto] >= 1:
            if producto in self.pedido:
                self.pedido[producto] += 1
                print(f'Se ha agregado el producto {producto.nombre}')
                self.mostrar_pedido()
            else:
                self.pedido[producto] = 1
                print(f'Se ha agregado el producto {producto.nombre}')
                self.mostrar_pedido()
        else:
            print(f'El producto {producto.nombre} no existe.')

    def eliminar_producto(self, producto, almacen):
        # quitarlo del pedido y agregarlo al almacen
        if producto in self.pedido:
            if self.pedido[producto] > 1:
                self.pedido[producto] -= 1
                almacen.productos[producto] += 1
                print(f'Se ha eliminado el producto {producto.nombre}')
                self.mostrar_pedido()
            else:
                nombre = producto.nombre
                del self.pedido[producto]
                print(f'Se ha eliminado el producto {nombre}')
                self.mostrar_pedido()

        else:
            print(f'El producto {producto.nombre} no existe en el pedido')
            self.mostrar_pedido()

    def mostrar_pedido(self):
        print('Pedido  \n')
        for producto, cantidad in self.pedido.items():
            print(f'{cantidad} {producto.nombre}: ${producto.precio*cantidad}')

    
    def tramitar_pedido(self, sistema, cliente):
        self.pedido_tramitado = {}
        # {pedido_id: {"productos": {producto: (cantidad, precio_unitario)}, "total": total, "fecha": fecha}}
        total = 0
        # hacer el total y lista de productos
        self.productos = {} # {producto : cantidad}
        for producto, cantidad in self.pedido.items():
            total += producto.precio * cantidad
            self.productos[producto.nombre] = cantidad

        hoy = date.today()
        hoy = hoy.strftime("%d/%m/%Y")
        self.pedido_tramitado[producto.id] = {
            'Fecha' : hoy,
            'Id Cliente': cliente.id,
            'Productos' : self.productos,
            'Total' : total
        }

        # agregarlo al sistema
        sistema.agregar_pedido_al_sistema(self.pedido_tramitado)

        # agregarlo al historial del cliente
        cliente.pedidos.append(self.pedido_tramitado)

        return self.pedido_tramitado

import json

class Sistema:
    def __init__(self):
        # {pedido_id: {"productos": {producto: cantidad}, "total": total, "fecha": fecha}}
        self.pedidos = []
        self.ids_usadas = set()
    
    def agregar_pedido_al_sistema(self, pedido):
        self.pedidos.append(pedido)

    def mostrar_pedidos_en_sistema(self):
        for pedido in self.pedidos:
            print(pedido)


# pueden tener descuento
class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio


class Almacen:
    def __init__(self):
        self.productos = {}
        # {producto : cantidad}
    
    def agregar_producto(self, producto):
        if producto in self.productos:
            self.productos[producto] += 1
        else:
            self.productos[producto] = 1
    
    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos[producto] -= 1
            print(f'Se ha eliminado el producto {producto.nombre}')
        else:
            print(f'No existe el producto {producto.nombre} en el almacen')

    def mostrar_productos_almacen(self):
        for producto, cantidad in self.productos.items():
            print(f'Producto: {producto.nombre}')
            print(f'Cantidad: {cantidad}')
            print(f'Precio: ${producto.precio}')


def main():
    almacen = Almacen()

    pasta = Producto(1, 'Pasta de dientes', 30.50)
    shampoo = Producto(2, 'Shampoo', 75.00)
    jabon = Producto(3, 'Jabón de tocador', 20.00)
    cepillo = Producto(4, 'Cepillo de dientes', 45.00)
    desodorante = Producto(5, 'Desodorante', 60.00)
    crema = Producto(6, 'Crema hidratante', 120.00)
    peine = Producto(7, 'Peine', 25.00)
    gel = Producto(8, 'Gel para el cabello', 55.00)
    rastrillo = Producto(9, 'Rastrillo', 35.00)
    enjuague = Producto(10, 'Enjuague bucal', 80.00)
    pañuelos = Producto(11, 'Pañuelos desechables', 18.00)
    locion = Producto(12, 'Loción para después de afeitar', 95.00)
    perfume = Producto(13, 'Perfume', 250.00)
    bloqueador = Producto(14, 'Bloqueador solar', 150.00)
    toallas = Producto(15, 'Toallas húmedas', 40.00)
    talco = Producto(16, 'Talco para pies', 38.00)
    algodon = Producto(17, 'Algodón en bolitas', 22.00)
    hisopos = Producto(18, 'Hisopos para oídos', 15.00)
    maquinilla = Producto(19, 'Maquinilla de afeitar', 70.00)
    cera = Producto(20, 'Cera para el cabello', 65.00)
    crema_manos = Producto(21, 'Crema para manos', 90.00)
    mascarilla = Producto(22, 'Mascarilla facial', 110.00)
    serum = Producto(23, 'Serum para la piel', 200.00)
    exfoliante = Producto(24, 'Exfoliante facial', 130.00)
    shampoo_seco = Producto(25, 'Shampoo en seco', 85.00)
    corta_unas = Producto(26, 'Cortaúñas', 28.00)
    cepillo_cabello = Producto(27, 'Cepillo para el cabello', 60.00)
    colonia = Producto(28, 'Colonia', 140.00)
    desinfectante = Producto(29, 'Desinfectante de manos', 55.00)
    balsamo_labial = Producto(30, 'Bálsamo labial', 35.00)

    almacen.agregar_producto(pasta)
    almacen.agregar_producto(shampoo)
    almacen.agregar_producto(jabon)
    almacen.agregar_producto(cepillo)
    almacen.agregar_producto(desodorante)
    almacen.agregar_producto(crema)
    almacen.agregar_producto(peine)
    almacen.agregar_producto(gel)
    almacen.agregar_producto(rastrillo)
    almacen.agregar_producto(enjuague)
    almacen.agregar_producto(pañuelos)
    almacen.agregar_producto(locion)
    almacen.agregar_producto(perfume)
    almacen.agregar_producto(bloqueador)
    almacen.agregar_producto(toallas)
    almacen.agregar_producto(talco)
    almacen.agregar_producto(algodon)
    almacen.agregar_producto(hisopos)
    almacen.agregar_producto(maquinilla)
    almacen.agregar_producto(cera)
    almacen.agregar_producto(crema_manos)
    almacen.agregar_producto(mascarilla)
    almacen.agregar_producto(serum)
    almacen.agregar_producto(exfoliante)
    almacen.agregar_producto(shampoo_seco)
    almacen.agregar_producto(corta_unas)
    almacen.agregar_producto(cepillo_cabello)
    almacen.agregar_producto(colonia)
    almacen.agregar_producto(desinfectante)
    almacen.agregar_producto(balsamo_labial)
    
    sistema = Sistema()
    #almacen.mostrar_productos_almacen()
    cliente1 = Cliente('Mariela')
    pedido = Pedido()
    pedido.agregar_producto(almacen, shampoo)
    pedido.agregar_producto(almacen, pasta)
    pedido.eliminar_producto(pasta, almacen)
    pedido.agregar_producto(almacen, exfoliante)
    pedido.agregar_producto(almacen, serum)
    pedido.agregar_producto(almacen, serum)
    pedido.tramitar_pedido(sistema, cliente1)
    sistema.mostrar_pedidos_en_sistema()

main()
