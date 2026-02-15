from servicios.inventario import Inventario
from modelos.producto import Producto

def main():
    inventario = Inventario()
    
    while True:
        print("\n===== MENÚ INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            
         elif opcion == "2":
            inventario.mostrar_productos()
            
        elif opcion == "3":
            id_producto = input("Ingrese el ID a buscar: ")
            producto = inventario.buscar_producto(id_producto)

            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")

