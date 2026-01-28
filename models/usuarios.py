from werkzeug.security import generate_password_hash, check_password_hash
from extensions import mysql

# Crear un nuevo usuario con contraseña encriptada
def crear_usuario(nombre_usuario, password, rol="usuario", activo=1):
    cur = mysql.connection.cursor()
    clave_hash = generate_password_hash(password)  # 🔒 Encriptar contraseña
    cur.execute("""
        INSERT INTO usuarios (nombre_usuario, clave_hash, rol, activo)
        VALUES (%s, %s, %s, %s)
    """, (nombre_usuario, clave_hash, rol, activo))
    mysql.connection.commit()
    cur.close()

# Obtener usuario por nombre
def obtener_usuario_por_nombre(nombre_usuario):
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT id, nombre_usuario, clave_hash, rol, activo
        FROM usuarios
        WHERE nombre_usuario = %s
    """, (nombre_usuario,))
    user = cur.fetchone()
    cur.close()
    return user

# Obtener usuario por nombre
def obtener_usuario_mysql(mysql,nombre_usuario):
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT id, nombre_usuario, clave_hash, rol, activo
        FROM usuarios
        WHERE nombre_usuario = %s
    """, (nombre_usuario,))
    user = cur.fetchone()
    cur.close()
    return user

# Validar contraseña ingresada contra el hash guardado
def validar_password(clave_hash, password):
    return check_password_hash(clave_hash, password)

# Opcional: listar todos los usuarios
def listar_usuarios():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nombre_usuario, rol, activo FROM usuarios")
    usuarios = cur.fetchall()
    cur.close()
    return usuarios

# Opcional: desactivar usuario
def desactivar_usuario(usuario_id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE usuarios SET activo = 0 WHERE id = %s", (usuario_id,))
    mysql.connection.commit()
    cur.close()
