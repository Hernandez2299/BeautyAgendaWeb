from extensions import mysql
import MySQLdb.cursors

# Crear un nuevo cliente
def crear_cliente(nombre, telefono, correo):
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO clientes (nombre, telefono, correo) VALUES (%s, %s, %s)",
            (nombre, telefono, correo)
        )
        mysql.connection.commit()
        cur.close()
        return True, None
    except Exception as e:
        return False, str(e)

# Obtener todos los clientes
def obtener_clientes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nombre, telefono, correo FROM clientes")
    clientes = cur.fetchall()
    cur.close()
    return clientes

# Obtener un cliente por ID
def obtener_cliente_por_id(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT id, nombre, telefono, correo FROM clientes WHERE id = %s", (id,))
    cliente = cur.fetchone()
    cur.close()
    return cliente

# Actualizar cliente
def actualizar_cliente(id, nombre, telefono, correo):
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE clientes SET nombre=%s, telefono=%s, correo=%s WHERE id=%s",
            (nombre, telefono, correo, id)
        )
        mysql.connection.commit()
        cur.close()
        return True, None
    except Exception as e:
        return False, str(e)

# Eliminar cliente
def eliminar_cliente(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM clientes WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
        return True, None
    except Exception as e:
        return False, str(e)
