from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.segurity import login_required, role_required
from models.clientes import obtener_clientes, crear_cliente, obtener_cliente_por_id, actualizar_cliente, eliminar_cliente

bp = Blueprint("clientes", __name__, url_prefix="/clientes")

# Listar clientes
@bp.route("/listar")
@login_required
@role_required('admin', 'recepcion')
def listar():
    clientes = obtener_clientes()
    return render_template("clientes.html", clientes=clientes)

# Crear cliente
@bp.route("/crear", methods=["GET", "POST"])
@login_required
@role_required('admin', 'recepcion')
def crear():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")
        correo = request.form.get("correo")

        try:
            crear_cliente(nombre, telefono, correo)
            flash("Cliente creado exitosamente", "success")
            return redirect(url_for("clientes.listar"))
        except Exception as e:
            flash("Error al crear cliente: " + str(e), "error")
            return redirect(url_for("clientes.crear"))

    return render_template("crear_cliente.html")

# Editar cliente
@bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
@role_required('admin', 'recepcion')
def editar(id):
    cliente = obtener_cliente_por_id(id)

    if request.method == "POST":
        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")
        correo = request.form.get("correo")

        try:
            actualizar_cliente(id, nombre, telefono, correo)
            flash("Cliente actualizado exitosamente", "success")
            return redirect(url_for("clientes.listar"))
        except Exception as e:
            flash("Error al actualizar cliente: " + str(e), "error")
            return redirect(url_for("clientes.editar", id=id))

    return render_template("editar_cliente.html", cliente=cliente)

# Eliminar cliente
@bp.route("/eliminar/<int:id>", methods=["POST"])
@login_required
@role_required('admin')
def eliminar(id):
    try:
        eliminar_cliente(id)
        flash("Cliente eliminado exitosamente", "success")
    except Exception as e:
        flash("Error al eliminar cliente: " + str(e), "error")

    return redirect(url_for("clientes.listar"))
