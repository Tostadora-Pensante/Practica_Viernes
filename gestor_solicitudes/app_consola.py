from flask import Flask, render_template, request, redirect, url_for, flash
import logica

app = Flask(__name__)
app.secret_key = "clave_secreta_para_mensajes"


@app.get("/")
def inicio():
    busqueda_resultado = None
    busqueda_ubicacion = None

    # Manejo de búsqueda por ID
    id_buscar = request.args.get("id_buscar")
    if id_buscar:
        try:
            id_num = int(id_buscar)
            busqueda_resultado, busqueda_ubicacion = logica.buscar_solicitud(id_num)
            if not busqueda_resultado:
                flash(f"No se encontró ninguna solicitud con el ID {id_num}.", "warning")
        except ValueError:
            flash("El ID ingresado para buscar debe ser un número entero.", "danger")

    siguiente = logica.consultar_siguiente()
    pendientes, historial_cant, total_unicas = logica.obtener_estadisticas()

    return render_template(
        "index.html",
        pendientes=logica.cola_pendientes,
        historial=logica.pila_historial,
        siguiente=siguiente,
        busqueda_resultado=busqueda_resultado,
        busqueda_ubicacion=busqueda_ubicacion,
        cant_pendientes=pendientes,
        cant_historial=historial_cant,
        total_unicas=total_unicas
    )


@app.post("/registrar")
def registrar():
    cliente = request.form.get("cliente", "")
    asunto = request.form.get("asunto", "")
    res = logica.registrar_solicitud(cliente, asunto)
    if res:
        flash(f"Solicitud #{res['id']} registrada con éxito.", "success")
    else:
        flash("No se pudo registrar: datos inválidos o solicitud duplicada en pendientes.", "danger")
    return redirect(url_for("inicio"))


@app.post("/atender")
def atender():
    res = logica.atender_siguiente()
    if res:
        flash(f"Solicitud #{res['id']} de {res['cliente']} atendida.", "info")
    else:
        flash("No hay solicitudes pendientes para atender.", "warning")
    return redirect(url_for("inicio"))


@app.post("/deshacer")
def deshacer():
    res = logica.deshacer_ultima_atencion()
    if res:
        flash(f"Se restauró la solicitud #{res['id']} a la cola de pendientes.", "info")
    else:
        flash("El historial está vacío, no hay atenciones que deshacer.", "warning")
    return redirect(url_for("inicio"))


@app.post("/deshacer_varias")
def deshacer_varias():
    try:
        cant = int(request.form.get("cantidad", 0))
        recuperadas = logica.deshacer_varias(cant)
        if recuperadas > 0:
            flash(f"Se deshicieron con éxito {recuperadas} atención(es).", "info")
        else:
            flash("No se deshizo ninguna atención (cantidad inválida o historial vacío).", "warning")
    except ValueError:
        flash("Por favor ingresa un número entero válido para la cantidad.", "danger")
    return redirect(url_for("inicio"))


@app.post("/cancelar")
def cancelar():
    try:
        id_num = int(request.form.get("id_cancelar", 0))
        res = logica.cancelar_solicitud(id_num)
        if res:
            flash(f"Solicitud #{id_num} cancelada correctamente.", "success")
        else:
            flash(f"No se encontró una solicitud pendiente con el ID {id_num}.", "warning")
    except ValueError:
        flash("El ID a cancelar debe ser un número entero.", "danger")
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)