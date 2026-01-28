from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from utils.segurity import *
from models.servicios import *

bp = Blueprint('servicios', __name__, url_prefix='/servicios')
@bp.route('/')
@login_required
@role_required('admin')

# Listar servicios

def listar():
    servicios = obtener_servicios()
    return render_template("servicios.html", servicios=servicios)

# Crear servicio
@bp.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        activo = request.form["activo"]

        crear_servicio(nombre, descripcion, precio, activo)
        flash("Servicio creado correctamente", "success")
        return redirect(url_for("servicios.listar"))

    return render_template("crear_servicios.html")

# Editar servicio
@bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    servicio = obtener_servicio(id)

    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        activo = request.form["activo"]

        editar_servicio(id, nombre, descripcion, precio, activo)
        flash("Servicio actualizado correctamente", "success")
        return redirect(url_for("servicios.listar"))

    return render_template("editar_servicios.html", servicio=servicio)

# Eliminar servicio
@bp.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    eliminar_servicio(id)
    flash("Servicio eliminado correctamente", "success")
    return redirect(url_for("servicios.listar"))

# Cambiar estado activo/inactivo
@bp.route("/cambiar_estado/<int:id>", methods=["POST"])
def cambiar_estado(id):
    cambiar_estado_servicio(id)
    flash("Estado del servicio actualizado correctamente", "success")
    return redirect(url_for("servicios.listar"))

