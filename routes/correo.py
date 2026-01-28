from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.correo import Recordatorio, MensajeInstitucional, PlantillaCorreo, HistorialCorreo
from datetime import datetime

bp = Blueprint("correo", __name__)

# Página principal de correos
@bp.route("/s_correo")
def s_correo():
    return render_template("s_correo.html")

# -------------------------------
# Recordatorios automáticos
# -------------------------------
@bp.route("/recordatorios")
def recordatorios():
    recordatorios = Recordatorio.get_all()
    return render_template("s_correo/recordatorios.html", recordatorios=recordatorios)

# -------------------------------
# Mensajes globales
# -------------------------------
@bp.route("/mensajes_globales", methods=["GET", "POST"])
def mensajes_globales():
    if request.method == "POST":
        asunto = request.form["asunto"]
        mensaje = request.form["mensaje"]

        MensajeInstitucional.insert(asunto, mensaje)

        flash("Mensaje institucional guardado y listo para enviar.", "success")
        return redirect(url_for("correo.mensajes_globales"))

    mensajes = MensajeInstitucional.get_all()
    return render_template("s_correo/mensajes_globales.html", mensajes=mensajes)

# -------------------------------
# Plantillas dinámicas
# -------------------------------
@bp.route("/plantillas", methods=["GET", "POST"])
def plantillas():
    if request.method == "POST":
        nombre = request.form["nombre"]
        contenido = request.form["contenido"]

        PlantillaCorreo.insert(nombre, contenido)

        flash("Plantilla creada/modificada con éxito.", "success")
        return redirect(url_for("correo.plantillas"))

    plantillas = PlantillaCorreo.get_all()
    return render_template("s_correo/plantillas.html", plantillas=plantillas)

# -------------------------------
# Historial de correos
# -------------------------------
@bp.route("/historial_correos")
def historial_correos():
    historial = HistorialCorreo.get_all()
    return render_template("s_correo/historial_correos.html", historial=historial)
