from flask import Blueprint, render_template, request, redirect, url_for, flash , jsonify
from models import citas
from extensions import mysql
from utils.segurity import *
import MySQLdb.cursors
from datetime import date
from datetime import datetime

bp = Blueprint("citas", __name__, url_prefix="/citas")

# =========================
# Listar citas
# =========================
@bp.route("/")
@login_required 
@role_required('admin','recepcion')
def listar():
    # Parámetros de filtro
    fecha = request.args.get("fecha")
    orden_hora = request.args.get("orden_hora", "asc")
    orden_fecha = request.args.get("orden_fecha", "asc")
    estado = request.args.get("estado", None)

    # Obtener citas filtradas desde el model
    data = citas.get_citas_filtradas(mysql, fecha, orden_hora, orden_fecha, estado)

    return render_template("citas.html", citas=data, current_date=date.today().strftime("%Y-%m-%d"))


# =========================
# Crear nueva cita
# =========================
@bp.route("/nueva", methods=["GET", "POST"])
@login_required
@role_required('admin','recepcion')
def nueva():
    if request.method == "POST":
        cliente_id = request.form.get("cliente_id")
        cliente_ocacional = request.form.get("cliente_ocacional")
        empleado_id = request.form.get("empleado_id")
        servicio_nombre = request.form.get("servicio_id")
        fecha = request.form.get("fecha")
        hora = request.form.get("hora")

        # Validación básica
        if not all([empleado_id, servicio_nombre, fecha, hora]):
            flash("Todos los campos son obligatorios", "error")
            return redirect(url_for("citas.nueva"))

        # Guardar cita usando el modelo
        ok, msg = citas.add_cita(
            mysql,
            cliente_id,
            empleado_id,
            servicio_nombre,
            fecha,
            hora,
            cliente_ocacional
        )

        if ok:
            flash("Cita registrada correctamente", "success")
            return redirect(url_for("citas.listar"))
        else:
            flash(msg or "Error al registrar la cita", "error")
            return redirect(url_for("citas.nueva"))

    # 👉 Parte GET: cargar listas dinámicas
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nombre FROM clientes")
    clientes = cur.fetchall()
    cur.execute("SELECT id, nombre FROM empleados WHERE activo = 1")
    empleados = cur.fetchall()
    cur.execute("SELECT nombre FROM servicios WHERE activo = 1")
    servicios = cur.fetchall()
    cur.close()

    return render_template("nueva_cita.html", empleados=empleados, servicios=servicios, clientes=clientes)

# =========================
# Editar cita
# =========================
@bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):
    if request.method == "POST":
        fecha = request.form.get("fecha")
        hora = request.form.get("hora")
        estado = request.form.get("estado")

        if not all([fecha, hora, estado]):
            flash("Todos los campos son obligatorios", "error")
            return redirect(url_for("citas.editar", id=id))

        citas.update_cita(mysql, id, fecha, hora, estado)
        flash("Cita actualizada correctamente", "success")
        return redirect(url_for("citas.listar"))

    cita = citas.get_cita_by_id(mysql, id)
    if cita is None:
        flash("La cita no existe", "error")
        return redirect(url_for("citas.listar"))

    return render_template("editar_cita.html", cita=cita)

# =========================
# Cancelar cita
# =========================
@bp.route("/cancelar/<int:id>")
@role_required('admin','recepcion')
def cancelar(id):
    citas.cancelar_cita(mysql, id)
    flash("Cita cancelada", "info")
    return redirect(url_for("citas.listar"))

# =========================
# API para obtener citas en formato JSON
# =========================
@bp.route("/api")
def api_citas():

    start = request.args.get("start")  # formato: YYYY-MM-DD
    end = request.args.get("end")      # formato: YYYY-MM-DD

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("""
        SELECT 
            citas.id,
            citas.cliente_id,
            citas.cliente_nombre_manual,
            empleados.nombre AS empleado,
            servicios.nombre AS servicio,
            citas.fecha,
            citas.hora,
            citas.estado,
            clientes.nombre AS cliente_nombre
        FROM citas
        LEFT JOIN clientes ON citas.cliente_id = clientes.id
        JOIN empleados ON citas.empleado_id = empleados.id
        JOIN servicios ON citas.servicio_id = servicios.id
        WHERE citas.fecha BETWEEN %s AND %s
    """, (start, end))
    citas = cur.fetchall()
    cur.close()

    eventos = []
    for c in citas:
        # Usar nombre manual si no hay cliente asociado
        nombre_cliente = c["cliente_nombre"] or c["cliente_nombre_manual"] or "Sin cliente"
        # Formatear hora correctamente 
        hora_iso = datetime.strptime(str(c["hora"]), "%H:%M:%S").time().isoformat()

        eventos.append({
            "id": c["id"],
            "title": f"{nombre_cliente} - {c['servicio']} ({c['estado']})",
            "start": f"{c['fecha']}T{hora_iso}",
            "backgroundColor": color_por_estado(c["estado"]),
            "borderColor": borde_por_estado(c["estado"]),
            "textColor": texto_por_estado(c["estado"]),
            "extendedProps": {
                "empleado": c["empleado"],
                "estado": c["estado"]
            }
        })

    return jsonify(eventos)

def color_por_estado(estado):
    estado = estado.lower()
    return {
        "pendiente": "#fff3cd",
        "confirmada": "#d4edda",
        "cancelada": "#f8d7da",
        "completada": "#cce5ff"
    }.get(estado, "#e2e3e5")

def borde_por_estado(estado):
    estado = estado.lower()
    return {
        "pendiente": "#856404",
        "confirmada": "#155724",
        "cancelada": "#721c24",
        "completada": "#004085"
    }.get(estado, "#6c757d")

def texto_por_estado(estado):
    estado = estado.lower()
    return {
        "pendiente": "#856404",
        "confirmada": "#155724",
        "cancelada": "#721c24",
        "completada": "#004085"
    }.get(estado, "#343a40")

