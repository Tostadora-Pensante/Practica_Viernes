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

    solicitud = {
        "id": siguiente_id,
        "cliente": cliente.strip(),
        "asunto": asunto.strip(),
        "estado": "pendiente"
    }
    cola_pendientes.append(solicitud)
    siguiente_id += 1
    return solicitud


registrar_solicitud("Ana", "No conecta a Wi-Fi")
registrar_solicitud("Luis", "Impresora sin papel")
registrar_solicitud("Sofía", "Equipo lento")
mostrar_estado()