from inventarioClass import datos_producto

class inventario_DAO:
    def __init__(self):
        self.lista_productos = []

    def agregar(self, nombre, cantidad, precio, ubicacion):
        producto_nuevo = datos_producto(nombre, cantidad, precio, ubicacion)
        self.lista_productos.append(producto_nuevo)
        print("Producto Agregado Correctamente")
        return True

    def encontrar_producto(self, nombre, ubicacion):
        for producto in self.lista_productos:
            if producto.nombre == nombre and producto.ubicacion == ubicacion:
                return producto
        return None

    def agregar_stock(self, nombre, ubicacion, cantidad):
        producto_existente = self.encontrar_producto(nombre, ubicacion)
        if producto_existente is not None:
            producto_existente.cantidad += cantidad
            print("Producto Actualizado Correctamente")
        else:
            print("Error: El producto",nombre,"no existe en la ubicación",ubicacion)

    def vender_producto(self, nombre, ubicacion, cantidad):
        producto_existente = self.encontrar_producto(nombre, ubicacion)
        if producto_existente is not None:
            if cantidad < producto_existente.cantidad:
                producto_existente.cantidad -= cantidad
                print("Producto Vendido Correctamente")
            elif cantidad >= producto_existente.cantidad:
                print("Error: La cantidad a vender de",nombre,"en la ubicación",ubicacion,"es mayor o igual que la existencia.")
        else:
            print("Error: El producto",nombre,"no existe en la ubicación",ubicacion)

    def imprimir(self):
        for producto in self.lista_productos:
            print(producto)
