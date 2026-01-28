from extensions import mysql
import MySQLdb.cursors

# Obtener todos los servicios
def obtener_servicios():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT id, nombre, descripcion, precio, activo FROM servicios")
    servicios = cur.fetchall()
    cur.close()
    return servicios

# Crear servicio
def crear_servicio(nombre, descripcion, precio, activo):
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO servicios (nombre, descripcion, precio, activo) VALUES (%s, %s, %s, %s)",
        (nombre, descripcion, precio, activo)
    )
    mysql.connection.commit()
    cur.close()

# Obtener servicio por ID
def obtener_servicio(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT id, nombre, descripcion, precio, activo FROM servicios WHERE id = %s", (id,))
    servicio = cur.fetchone()
    cur.close()
    return servicio

# Editar servicio
def editar_servicio(id, nombre, descripcion, precio, activo):
    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE servicios SET nombre=%s, descripcion=%s, precio=%s, activo=%s WHERE id=%s",
        (nombre, descripcion, precio, activo, id)
    )
    mysql.connection.commit()
    cur.close()

# Eliminar servicio
def eliminar_servicio(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM servicios WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()

# Cambiar estado activo/inactivo
def cambiar_estado_servicio(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT activo FROM servicios WHERE id = %s", (id,))
    servicio = cur.fetchone()

    if servicio:
        nuevo_estado = 0 if servicio["activo"] == 1 else 1
        cur2 = mysql.connection.cursor()
        cur2.execute("UPDATE servicios SET activo = %s WHERE id = %s", (nuevo_estado, id))
        mysql.connection.commit()
        cur2.close()

    cur.close()
