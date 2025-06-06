from finanzas import obtener_balance
from utils import cargar_json, guardar_json
from estrategias.porcentaje_fijo import PorcentajeFijoStrategy
from estrategias.agresivo import AhorroAgresivoStrategy
from estrategias.conservador import AhorroConservadorStrategy


METAS_FILE = "datos/metas.json"

def seleccionar_estrategia():
    print("\nSelecciona una estrategia de ahorro:")
    print("1. Porcentaje Fijo (30%)")
    print("2. Ahorro Agresivo (50%)")
    print("3. Ahorro Conservador (10%)")
    opcion = input("Opción: ")

    if opcion == "2":
        return AhorroAgresivoStrategy()
    elif opcion == "3":
        return AhorroConservadorStrategy()
    else:
        return PorcentajeFijoStrategy()


def registrar_meta(usuario):
    metas = cargar_json(METAS_FILE)

    print("\n--- Registrar Meta Financiera ---")

    nombre_meta = input("Ingresa el nombre de la meta: ").strip()
    monto_objetivo = float(input("Ingresa el monto objetivo de la meta: "))

    # Preguntar ingreso mensual fijo
    ingreso_fijo = float(input("¿Cuál es tu ingreso mensual fijo? "))
    estrategia = seleccionar_estrategia()
    cuota_sugerida = estrategia.calcular_cuota(ingreso_fijo)


    print(f"\nSe recomienda una cuota mensual de: ${cuota_sugerida:.2f} según la estrategia seleccionada.")


    cuota_mensual = input(f"¿Cuánto puedes ahorrar mensualmente? (Recomendado: ${cuota_sugerida:.2f}): ")
    cuota_mensual = float(cuota_mensual) if cuota_mensual else cuota_sugerida

    # Calcular el tiempo estimado
    tiempo_estimado = monto_objetivo / cuota_mensual

    # Crear y guardar la meta
    nueva_meta = {
        "usuario": usuario["nombre"],
        "nombre_meta": nombre_meta,
        "monto_objetivo": monto_objetivo,
        "cuota_mensual": cuota_mensual,
        "tiempo_estimado": round(tiempo_estimado, 2)
    }

    metas.append(nueva_meta)
    guardar_json(METAS_FILE, metas)
    print(f"\nMeta '{nombre_meta}' registrada con éxito. Tiempo estimado: {round(tiempo_estimado, 2)} meses.")


def ver_metas(usuario):
    metas = cargar_json(METAS_FILE)
    print("\n--- Mis Metas ---")
    metas_usuario = [meta for meta in metas if meta["usuario"] == usuario["nombre"]]
    
    if not metas_usuario:
        print("No tienes metas registradas.")
    else:
        for meta in metas_usuario:
            print(f"\nNombre: {meta['nombre_meta']}")
            print(f"Monto objetivo: ${meta['monto_objetivo']}")
            print(f"Cuota mensual: ${meta['cuota_mensual']}")
            print(f"Tiempo estimado: {meta['tiempo_estimado']} meses")


def eliminar_meta(usuario):
    metas = cargar_json(METAS_FILE)
    metas_usuario = [meta for meta in metas if meta["usuario"] == usuario["nombre"]]

    if not metas_usuario:
        print("No tienes metas registradas.")
        return

    print("\n--- Eliminar Meta ---")
    for i, meta in enumerate(metas_usuario, 1):
        print(f"{i}. {meta['nombre_meta']}")

    opcion = input("Selecciona el número de la meta a eliminar: ")
    if not opcion.isdigit() or not (1 <= int(opcion) <= len(metas_usuario)):
        print("Opción inválida.")
        return

    meta_eliminar = metas_usuario[int(opcion) - 1]
    metas.remove(meta_eliminar)
    guardar_json(METAS_FILE, metas)
    print(f"Meta '{meta_eliminar['nombre_meta']}' eliminada correctamente.")


def editar_meta(usuario):
    metas = cargar_json(METAS_FILE)
    metas_usuario = [m for m in metas if m["usuario"] == usuario["nombre"]]

    if not metas_usuario:
        print("\nNo tienes metas para editar.")
        return

    print("\n--- Editar Meta ---")
    for idx, meta in enumerate(metas_usuario, start=1):
        print(f"{idx}. {meta['nombre_meta']}")

    opcion = input("Selecciona el número de la meta a editar: ")
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(metas_usuario):
        print("Selección inválida.")
        return

    meta_elegida = metas_usuario[int(opcion) - 1]

    # Editar campos
    nuevo_nombre = input(f"Nuevo nombre (actual: {meta_elegida['nombre_meta']}): ").strip()
    nuevo_monto = input(f"Nuevo monto objetivo (actual: {meta_elegida['monto_objetivo']}): ")
    nueva_cuota = input(f"Nueva cuota mensual (actual: {meta_elegida['cuota_mensual']}): ")

    if nuevo_nombre:
        meta_elegida['nombre_meta'] = nuevo_nombre
    if nuevo_monto:
        meta_elegida['monto_objetivo'] = float(nuevo_monto)
    if nueva_cuota:
        meta_elegida['cuota_mensual'] = float(nueva_cuota)

    # Recalcular tiempo estimado
    if nueva_cuota or nuevo_monto:
        try:
            meta_elegida['tiempo_estimado'] = round(
                meta_elegida['monto_objetivo'] / meta_elegida['cuota_mensual'], 2
            )
        except ZeroDivisionError:
            meta_elegida['tiempo_estimado'] = 0

    # Reemplazar en la lista original
    for i in range(len(metas)):
        if metas[i]["usuario"] == usuario["nombre"] and metas[i]["nombre_meta"] == metas_usuario[int(opcion) - 1]["nombre_meta"]:
            metas[i] = meta_elegida
            break

    guardar_json(METAS_FILE, metas)
    print("Meta actualizada correctamente.")
