import persistencia
import funciones as fn

def main():
    inventario=persistencia.cargar_inventario()
    while True:
        eleccion=fn.mostrar_menu()
        if(eleccion==1):
            fn.agregar_producto(inventario)
            persistencia.guardar_inventario(inventario)
        elif(eleccion==2):
            fn.lista_productos(inventario)
        elif(eleccion==3):
            fn.actualizar_stock(inventario)
            persistencia.guardar_inventario(inventario)
        elif(eleccion==4):
            fn.busca_producto(inventario)
        elif(eleccion==5):
            fn.eliminar_producto(inventario)
            persistencia.guardar_inventario(inventario)
        elif eleccion==6:
            fn.reporte_valor_inventario(inventario)
            total = sum(item['precio'] * item['cantidad'] for item in inventario)
            print(f"El valor total del inventario es: {total}")
        elif eleccion==7:
            print("haz elegido salir del programa ")
            break
        else:
            print("opcion no valida ")

main()   




