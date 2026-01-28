from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.segurity import login_required, role_required
from models.empleados import (
    obtener_empleados,
    crear_empleado,
    obtener_empleado,
    editar_empleado,
    eliminar_empleado,
    cambiar_estado_empleado
)

bp = Blueprint('empleados', __name__, url_prefix='/empleados')

# Listar empleados
@bp.route('/')
@login_required
@role_required('admin')
def listar():
    empleados = obtener_empleados()
    return render_template("empleados.html", empleados=empleados)

# Crear empleado
@bp.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        especialidad = request.form["especialidad"]
        activo = request.form["activo"]

        crear_empleado(nombre, especialidad, activo)
        flash("Empleado creado correctamente", "success")
        return redirect(url_for("empleados.listar"))

    return render_template("crear_empleado.html")

# Editar empleado
@bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    empleado = obtener_empleado(id)

    if request.method == "POST":
        nombre = request.form.get("nombre")
        especialidad = request.form.get("especialidad")
        activo = request.form.get("activo")

        try:
            editar_empleado(id, nombre, especialidad, activo)
            flash("Empleado actualizado exitosamente", "success")
            return redirect(url_for("empleados.listar"))
        except Exception as e:
            flash("Error al actualizar empleado: " + str(e), "error")
            return redirect(url_for("empleados.listar", id=id))

    return render_template("editar_empleados.html", empleado=empleado)


# Eliminar empleado
@bp.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    eliminar_empleado(id)
    flash("Empleado eliminado correctamente", "success")
    return redirect(url_for("empleados.listar"))

# Cambiar estado activo/inactivo
@bp.route("/cambiar_estado/<int:id>", methods=["POST"])
def cambiar_estado(id):
    cambiar_estado_empleado(id)
    flash("Estado del empleado actualizado correctamente", "success")
    return redirect(url_for("empleados.listar"))
