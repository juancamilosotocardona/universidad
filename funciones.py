def mostrar_menu():
    print("\n---sistema gestor de inventario---")
    print("1. agregar producto")
    print("2. lista de todos los producto ")
    print("3. actualizar stock de un producto")
    print("4. buscar un producto")
    print("5. eliminar un producto")
    print("6. valor total del inventario")
    print("7. salir")
    try:
     opcion=int(input("ingrese una opcion:"))
     return opcion
    except ValueError:
        print("tienes que ingresar un numero")

def agregar_producto(lista):
    nombre=input("ingrese el nombre del producto:")
    try:
        cantidad=int(input("ingrese la cantidad del producto:"))
        precio=float(input("ingrese el precio del producto:"))
        marca=input("ingrese la marca del producto:")
        nuevo_producto={"nombre":nombre,"cantidad":cantidad,"precio":precio,"marca":marca}
        lista.append(nuevo_producto)
    except ValueError:
        print("tienes que ingresar un numero")

def lista_productos(lista):
    if not lista:
        print("No hay productos en el inventario.")
        return
    print("\n--- Lista de Productos ---")
    for i in lista:
        print(f"{i}. [Nombre:] {i['nombre']}, Cantidad: {i['cantidad']}, Precio: {i['precio']}, Marca: {i['marca']}")
        print("-------------------------")

def encontrar_producto(lista, nombre):
    for producto in lista:
        if producto['nombre'].lower() == nombre.lower():
            return producto
    return None

def actualizar_stock(lista):
   
    nombre = input("ingrese el nombre del producto a actualizar: ")
    producto = encontrar_producto(lista, nombre)
    if producto:
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            producto['cantidad'] = nueva_cantidad
            print(f"Stock actualizado: {producto['nombre']}, Nueva Cantidad: {producto['cantidad']}, Precio: {producto['precio']}, Marca: {producto['marca']}")
        except ValueError:
            print("tienes que ingresar un numero")
    else:
        print(f"Producto {nombre} no encontrado.")

def busca_producto(lista):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    producto = encontrar_producto(lista, nombre)
    if producto:
        print(f"Producto encontrado: Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}, Marca: {producto['marca']}")
    else:
        print(f"Producto {nombre} no encontrado.")

def eliminar_producto(lista):
    nombre_eliminar= input("ingrese el nombre del producto a eliminar: ")
    producto=encontrar_producto(lista,nombre_eliminar)
    if producto:
        confirmacion=input(f"estas seguro que quieres eliminar el producto {producto['nombre']}? (si/no): ").lower()
        if confirmacion=="si":
            lista.remove(producto)
            print(f"producto {nombre_eliminar} eliminado exitosamente")
        else:
            print("eliminacion cancelada")
    else:
        print(f"producto {nombre_eliminar} no encontrado")


def reporte_valor_inventario(lista):
    if not lista:
        print("no hay productos en el inventario")
        return
    print("\n--- valor total del inventario ---")
    for producto in lista:
        valor_total=producto['precio']*producto['cantidad']
        valor_total+=valor_total
        print(f"valor total del inventario: {valor_total}")
