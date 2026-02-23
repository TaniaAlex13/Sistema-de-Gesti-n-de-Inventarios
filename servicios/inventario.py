import os
from modelos.producto import Producto

class Inventario:

    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # ==============================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ==============================
    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()

            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")

                    if len(datos) == 4:
                        id_producto = datos[0]
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])

                        producto = Producto(id_producto, nombre, cantidad, precio)
                        self.productos.append(producto)

        except FileNotFoundError:
            print("Archivo no encontrado.")
        except PermissionError:
            print("No tienes permisos para acceder al archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")

    # ==============================
    # GUARDAR INVENTARIO EN ARCHIVO
    # ==============================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    linea = f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n"
                    file.write(linea)
            return True

        except PermissionError:
            print("No tienes permisos para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar archivo: {e}")
            return False

    # ==============================
    # BUSCAR PRODUCTO
    # ==============================
    def buscar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    # ==============================
    # AGREGAR PRODUCTO
    # ==============================
    def agregar_producto(self, producto):
        if self.buscar_producto(producto.get_id()):
            print("Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            if self.guardar_en_archivo():
                print("Producto agregado y guardado correctamente.")

    # ==============================
    # MOSTRAR PRODUCTOS
    # ==============================
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)

    # ==============================
    # ELIMINAR PRODUCTO
    # ==============================
    def eliminar_producto(self, id_producto):
        producto = self.buscar_producto(id_producto)
        if producto:
            self.productos.remove(producto)
            if self.guardar_en_archivo():
                print("Producto eliminado y archivo actualizado.")
        else:
            print("Producto no encontrado.")

