from extensions import mysql
import MySQLdb.cursors

# Obtener todos los empleados
def obtener_empleados():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT id, nombre, especialidad, activo FROM empleados")
    empleados = cur.fetchall()
    cur.close()
    return empleados

# Crear empleado
def crear_empleado(nombre, especialidad, activo):
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO empleados (nombre, especialidad, activo) VALUES (%s, %s, %s)",
        (nombre, especialidad, activo)
    )
    mysql.connection.commit()
    cur.close()

# Obtener empleado por ID
def obtener_empleado(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT id, nombre, especialidad, activo FROM empleados WHERE id = %s", (id,))
    empleado = cur.fetchone()
    cur.close()
    return empleado

# Editar empleado
def editar_empleado(id, nombre, especialidad, activo):
    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE empleados SET nombre=%s, especialidad=%s, activo=%s WHERE id=%s",
        (nombre, especialidad, activo, id)
    )
    mysql.connection.commit()
    cur.close()

# Eliminar empleado
def eliminar_empleado(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM empleados WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()

# Cambiar estado activo/inactivo
def cambiar_estado_empleado(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT activo FROM empleados WHERE id = %s", (id,))
    empleado = cur.fetchone()

    if empleado:
        nuevo_estado = 0 if empleado["activo"] == 1 else 1
        cur2 = mysql.connection.cursor()
        cur2.execute("UPDATE empleados SET activo = %s WHERE id = %s", (nuevo_estado, id))
        mysql.connection.commit()
        cur2.close()

    cur.close()
