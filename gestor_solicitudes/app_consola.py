# Ejercicio de ejemplo 1.
cola_pendientes = []
pila_historial = []
siguiente_id = 1


def mostrar_estado():
    print("\nPendientes:", cola_pendientes)
    print("Historial:", pila_historial)


def registrar_solicitud(cliente, asunto):
    global siguiente_id
    if not cliente.strip() or not asunto.strip():
        return None

    clienteunico = cliente.strip().lower()
    asuntounico = asunto.strip().lower()

    # Reto 5: Evitar duplicados en pendientes
    for solicitud in cola_pendientes:
        if (
            solicitud["cliente"].strip().lower() == clienteunico
            and solicitud["asunto"].strip().lower() == asuntounico
        ):
            return None

    solicitud = {
        "id": siguiente_id,
        "cliente": cliente.strip(),
        "asunto": asunto.strip(),
        "estado": "pendiente",
    }
    cola_pendientes.append(solicitud)
    siguiente_id += 1
    return solicitud


# registrar_solicitud("Ana", "No conecta a Wi-Fi")
# registrar_solicitud("Luis", "Impresora sin papel")
# registrar_solicitud("Sofía", "Equipo lento")
# mostrar_estado()

print("=" * 20)


def atender_siguiente():
    if not cola_pendientes:
        return None

    solicitud = cola_pendientes.pop(0)
    solicitud["estado"] = "atendida"
    pila_historial.append(solicitud)
    return solicitud


# print("Atendida:", atender_siguiente())
# mostrar_estado()


def deshacer_ultima_atencion():
    if not pila_historial:
        return None

    solicitud = pila_historial.pop()
    solicitud["estado"] = "pendiente"
    cola_pendientes.insert(0, solicitud)
    return solicitud


# print("Restaurada:", deshacer_ultima_atencion())
# mostrar_estado()
# si se atendió a Ana y después a Luis, el primer deshacer devuelve a Luis al inicio; otro deshacer devuelve a Ana antes que Luis. ¿Por qué?
# R: Porque la pila sigue el principio del LIFO, por lo que el ultimo elemento agregado a la pila es el primer eliminado, por ende al deshacer la ultima atencion, se restaura primero a luis y luego a ana


# Reto 1: Consultar el siguiente turno sin extraerlo
def consultar_siguiente():
    if not cola_pendientes:
        return None
    return cola_pendientes[0]


# Reto 2: Buscar una solicitud por ID
def buscar_solicitud(id_solicitud):
    for solicitud in cola_pendientes:
        if solicitud["id"] == id_solicitud:
            return solicitud, "pendiente"
    for solicitud in pila_historial:
        if solicitud["id"] == id_solicitud:
            return solicitud, "historial"
    return None


# Reto 3: Cancelar una solicitud pendiente
def cancelar_solicitud(id_solicitud):
    for solicitud in cola_pendientes:
        if solicitud["id"] == id_solicitud:
            cola_pendientes.remove(solicitud)
            solicitud["estado"] = "cancelada"
            return solicitud
    return None


# Reto 4: Deshacer varias atenciones
def deshacer_varias(cantidad):
    if cantidad <= 0:
        return 0

    recuperadas = 0
    for _ in range(cantidad):
        resultado = deshacer_ultima_atencion()
        if resultado is not None:
            recuperadas += 1
        else:
            break
    return recuperadas


def ejecutar_menu():
    while True:
        print("\n1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Deshacer última atención")
        print("4. Mostrar estado")
        print("5. Consultar Siguiente")
        print("6. Buscar ID")
        print("7. Cancelar solicitud")
        print("8. Deshacer varias atenciones")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cliente = input("Cliente: ")
            asunto = input("Asunto: ")
            resultado = registrar_solicitud(cliente, asunto)
            print("Registrada:", resultado if resultado else "Datos inválidos o duplicados")
        elif opcion == "2":
            print("Atendida:", atender_siguiente())
        elif opcion == "3":
            print("Restaurada:", deshacer_ultima_atencion())
        elif opcion == "4":
            mostrar_estado()
        elif opcion == "5":
            print("el siguiente en la cola es:", consultar_siguiente())
        elif opcion == "6":
            try:
                id = int(input("Ingrese el id a buscar: "))
                resultado = buscar_solicitud(id)
                if resultado:
                    solicitud, ubicacion = resultado
                    print(f"ID encontrado en ubicacion [{ubicacion}]:", solicitud)
                else:
                    print("No se encontro ninguna solicitud con ese ID")
            except ValueError:
                print(
                    "El id no es valido, tiene que ser un numero entero, pruebe de nuevo."
                )
        elif opcion == "7":
            try:
                id = int(input("Ingrese el ID a cancelar: "))
                resultado = cancelar_solicitud(id)
                if resultado:
                    print(f"Solicitud cancelada con exito", resultado)
                else:
                    print("No se encontraron solicitudes con ese ID")
            except ValueError:
                print("El id ingresado no es valido, ingrese un numero entero.")
        elif opcion == "8":
            try:
                cantidad = int(
                    input("Ingrese la cantidad de atenciones a deshacer: ")
                )
                if cantidad <= 0:
                    print("La cantidad debe ser un número entero positivo.")
                else:
                    recuperadas = deshacer_varias(cantidad)
                    print(
                        f"Se deshicieron con éxito {recuperadas} atención(es)."
                    )

            except ValueError:
                print(
                    "Por favor, ingrese un número entero válido para la cantidad."
                )
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    ejecutar_menu()