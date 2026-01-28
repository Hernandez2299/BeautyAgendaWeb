from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.usuarios import crear_usuario, obtener_usuario_mysql
from extensions import mysql
from werkzeug.security import check_password_hash

bp = Blueprint("usuarios", __name__, url_prefix="/usuarios/crear")

@bp.route("/", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        role = request.form.get("role")
        active = request.form.get("active")
        admin_key = request.form.get("admin_key")  # contraseña del admin ingresada en el formulario

        # Buscar al usuario admin en la BD
        admin_user = obtener_usuario_mysql(mysql, "admin")
        if not admin_user or not check_password_hash(admin_user[2], admin_key):
            flash("Contraseña de administrador incorrecta", "error")
            return redirect(url_for("usuarios.crear"))

        # Validar contraseñas
        if password != confirm_password:
            flash("Las contraseñas no coinciden", "error")
            return redirect(url_for("usuarios.crear"))

        try:
            crear_usuario(username, password, role, active)
            flash("Usuario creado exitosamente", "success")
            return redirect(url_for("usuarios.crear"))
        except Exception as e:
            flash("Error al crear usuario: " + str(e), "error")
            return redirect(url_for("usuarios.crear"))

    return render_template("crear_usuario.html")
