from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.usuarios import obtener_usuario_por_nombre, validar_password

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Buscar usuario en la BD
        user = obtener_usuario_por_nombre(username)

        # Validar usuario y contraseña
        if user and user[4] == 1 and validar_password(user[2], password):
            session["usuario_id"] = user[0]
            session["usuario_nombre"] = user[1]
            session["usuario_rol"] = user[3]
            flash("Bienvenido, " + user[1], "success")
            return redirect(url_for("index"))
        else:
            flash("Usuario o contraseña incorrectos", "error")
            return redirect(url_for("auth.login"))

    # Si es GET, mostramos el formulario
    return render_template("login.html")

@bp.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada correctamente", "info")
    return redirect(url_for("auth.login"))
