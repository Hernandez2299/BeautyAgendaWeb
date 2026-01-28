from flask import Flask, redirect, session, url_for
from extensions import mysql
from flask import render_template

# Inicializar aplicación Flask
app = Flask(__name__)
app.config.from_object('config') 

# Inicializar conexión MySQL
mysql.init_app(app)

# Importar y registrar blueprints (rutas)
from routes import citas, clientes, empleados, servicios, auth,crear_usuario,prueba, correo

app.register_blueprint(citas.bp)
app.register_blueprint(clientes.bp)
app.register_blueprint(empleados.bp)
app.register_blueprint(servicios.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(crear_usuario.bp)
app.register_blueprint(prueba.bp)
app.register_blueprint(correo.bp)

# Ruta principal
@app.route("/")
def index():
    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template("index.html", usuario=session["usuario_nombre"])



# Punto de entrada
if __name__ == "__main__":
    app.run(debug=True)
