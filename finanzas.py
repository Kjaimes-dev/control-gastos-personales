import datetime
from utils import cargar_json, guardar_json

MOVIMIENTOS_FILE = "datos/movimientos.json"

def registrar_movimiento(usuario, tipo):
    movimientos = cargar_json(MOVIMIENTOS_FILE)

    try:
        monto = float(input(f"Ingresar monto del {tipo}: "))
        if monto <= 0:
            print("El monto debe ser positivo.")
            return
    except ValueError:
        print("Monto inválido.")
        return

    descripcion = input("Descripción del movimiento: ").strip()
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nuevo = {
        "usuario": usuario["nombre"],
        "tipo": tipo,
        "monto": monto,
        "descripcion": descripcion,
        "fecha": fecha
    }

    movimientos.append(nuevo)
    guardar_json(MOVIMIENTOS_FILE, movimientos)
    print(f"{tipo.capitalize()} registrado correctamente.")


def ver_movimientos(usuario):
    movimientos = cargar_json(MOVIMIENTOS_FILE)
    user_movs = [m for m in movimientos if m["usuario"] == usuario["nombre"]]

    if not user_movs:
        print("No hay movimientos registrados.")
        return

    total_ingresos = 0
    total_gastos = 0

    print("\n--- Tus movimientos ---")
    for m in user_movs:
        print(f"[{m['fecha']}] {m['tipo'].capitalize()}: ${m['monto']} - {m['descripcion']}")
        if m["tipo"] == "ingreso":
            total_ingresos += m["monto"]
        elif m["tipo"] == "gasto":
            total_gastos += m["monto"]

    balance = total_ingresos - total_gastos

    print("\n--- Resumen financiero ---")
    print(f"Total ingresos: ${total_ingresos}")
    print(f"Total gastos:   ${total_gastos}")
    print(f"Balance:        ${balance}")

def obtener_balance(usuario):
    ingresos = cargar_json("datos/movimientos.json")
    ingresos_totales = sum(i['monto'] for i in ingresos if i['tipo'] == 'ingreso' and i['usuario'] == usuario["nombre"])
    gastos_totales = sum(i['monto'] for i in ingresos if i['tipo'] == 'gasto' and i['usuario'] == usuario["nombre"])
    return ingresos_totales - gastos_totales
