from flask import Blueprint, render_template

bp = Blueprint("prueba", __name__, url_prefix="/prueba")

@bp.route("/")
def index():
    return render_template("prueba.html")
