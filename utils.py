import json
import os

def cargar_json(ruta):
    # Crear archivo si no existe
    if not os.path.exists(ruta):
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4, ensure_ascii=False)
        return []

    with open(ruta, 'r', encoding='utf-8') as f:
        try:
            datos = json.load(f)
            # Validar que sea una lista
            if isinstance(datos, list):
                return datos
            else:
                print(f"Advertencia: {ruta} no contiene una lista válida. Se reiniciará.")
                return []
        except json.JSONDecodeError:
            print(f"Advertencia: El archivo {ruta} está corrupto o vacío. Se reiniciará.")
            return []

def guardar_json(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
