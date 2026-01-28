from flask import current_app
from extensions import mysql
import MySQLdb.cursors

# -------------------------------
# Recordatorio
# -------------------------------
class Recordatorio:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM recordatorios ORDER BY fecha_envio ASC")
        data = cur.fetchall()
        cur.close()
        return data

    @staticmethod
    def get_by_cita(cita_id):
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM recordatorios WHERE cita_id = %s", (cita_id,))
        data = cur.fetchone()
        cur.close()
        return data

    @staticmethod
    def insert(cita_id, fecha_envio):
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO recordatorios (cita_id, fecha_envio, enviado) VALUES (%s, %s, %s)",
            (cita_id, fecha_envio, False)
        )
        mysql.connection.commit()
        cur.close()

# -------------------------------
# Mensajes institucionales
# -------------------------------
class MensajeInstitucional:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM mensajes_institucionales ORDER BY fecha_creacion DESC")
        data = cur.fetchall()
        cur.close()
        return data

    @staticmethod
    def insert(asunto, contenido):
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO mensajes_institucionales (asunto, contenido, fecha_creacion) VALUES (%s, %s, NOW())",
            (asunto, contenido)
        )
        mysql.connection.commit()
        cur.close()

# -------------------------------
# Plantillas de correo
# -------------------------------
class PlantillaCorreo:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM plantillas_correo ORDER BY fecha_modificacion DESC")
        data = cur.fetchall()
        cur.close()
        return data

    @staticmethod
    def insert(nombre, contenido_html):
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO plantillas_correo (nombre, contenido_html, fecha_modificacion) VALUES (%s, %s, NOW())",
            (nombre, contenido_html)
        )
        mysql.connection.commit()
        cur.close()

# -------------------------------
# Historial de correos
# -------------------------------
class HistorialCorreo:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM historial_correos ORDER BY fecha_envio DESC")
        data = cur.fetchall()
        cur.close()
        return data

    @staticmethod
    def insert(destinatario, asunto, contenido, estado="pendiente"):
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO historial_correos (destinatario, asunto, contenido, fecha_envio, estado) VALUES (%s, %s, %s, NOW(), %s)",
            (destinatario, asunto, contenido, estado)
        )
        mysql.connection.commit()
        cur.close()
