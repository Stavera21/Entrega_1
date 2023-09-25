class Producto:
    def __init__(self,codigo:int, nombre:str, descripcion:str, categoria:str):
        self.codigo:int = codigo
        self.nombre:str = nombre
        self.descripcion:str = descripcion
        self.categoria:str = categoria

class Precio:
    def __init__(self,precio_compra:int, costo_venta:int):
        self.precio_compra:int = precio_compra
        self.costo_venta:int = costo_venta

    def calcular_porcentaje(self):
        return ((self.costo_venta - self.precio_compra) / (self.precio_compra)) * 100

class Inventario:
    def __init__(self)-> dict:
        self.inventario:dict = {}

    def agregar_productos(self,producto:str, cantidad:str):
        if producto not in self.inventario:
            self.inventario[producto.codigo] = {'producto': producto, 'cantidad': cantidad}
        else:
            self.inventario[producto.codigo]['cantidad']+= cantidad
        
        if producto.codigo not in self.inventario:
            self.inventario[producto.codigo] = {'producto': producto, 'cantidad': cantidad}
        else:
            print(f"Error! El producto con codigo {producto.codigo} ya existe en el inventario.")


    def eliminar_producto(self, codigo_producto:int):
        if codigo_producto in self.inventario:
            del self.inventario[codigo_producto]

#IMPLEMENTACION PARA AGREGAR Y/0 ELIMIMINAR PRODUCTOS.

'''
if __name__ == "__main__":
    producto1 = Producto("001", "Producto A", "Descripción del Producto A", "Categoría A")
    precio1 = Precio(10.0, 20.0)
    inventario = Inventario()

    inventario.agregar_producto(producto1, 50)
    inventario.eliminar_producto("001")

    ganancia = precio1.calcular_porcentaje_ganancia()
    print(f"Porcentaje de Ganancia: {ganancia}%")
'''
