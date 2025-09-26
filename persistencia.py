import json

def guardar_inventario(lista):
    with open("inventario.json", 'w') as archivo:
        json.dump(lista, archivo, indent=4)
    print("inventario guardado")


def cargar_inventario():
    try:
        with open("inventario.json", 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    