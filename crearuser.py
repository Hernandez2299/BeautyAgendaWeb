from app import app
from models.usuarios import crear_usuario

# Ejecutar dentro del contexto de Flask
with app.app_context():
    crear_usuario("jereck", "1234", rol="empleado")
    print("Usuario jereck creado correctamente")