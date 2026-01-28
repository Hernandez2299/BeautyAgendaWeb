from datetime import datetime, timedelta

# =========================
# Listar todas las citas
# =========================
def get_citas_filtradas(mysql, fecha=None, orden_hora="asc", orden_fecha="asc", estado=None):
    cur = mysql.connection.cursor()

    query = """
        SELECT 
            citas.id,
            clientes.nombre AS cliente,
            empleados.nombre AS empleado,
            servicios.nombre AS servicio,
            citas.fecha,
            citas.hora,
            citas.estado,
            citas.cliente_id,
            citas.cliente_nombre_manual
        FROM citas
        JOIN clientes ON citas.cliente_id = clientes.id
        JOIN empleados ON citas.empleado_id = empleados.id
        JOIN servicios ON citas.servicio_id = servicios.id
    """
    params = []

    # Si hay fecha, filtra; si no, muestra todo
    if fecha:
        query += " WHERE citas.fecha = %s"
        params.append(fecha)

    # Si hay estado, agrega condición
    if estado:
        if "WHERE" in query:
            query += " AND citas.estado = %s"
        else:
            query += " WHERE citas.estado = %s"
        params.append(estado)

    # Orden dinámico
    order_clauses = []
    if orden_fecha:
        order_clauses.append(f"citas.fecha {orden_fecha.upper()}")
    if orden_hora:
        order_clauses.append(f"citas.hora {orden_hora.upper()}")

    if order_clauses:
        query += " ORDER BY " + ", ".join(order_clauses)

    cur.execute(query, tuple(params))
    data = cur.fetchall()
    cur.close()
    return data


# =========================
def get_all_citas(mysql):
    cur = mysql.connection.cursor()
    cur.execute("""
    SELECT 
    citas.id,
    clientes.nombre AS cliente,
    empleados.nombre AS empleado,
    servicios.nombre AS servicio,
    citas.fecha,
    citas.hora,
    citas.estado,
    citas.cliente_id,
    citas.cliente_nombre_manual
    FROM citas
    JOIN clientes ON citas.cliente_id = clientes.id
    JOIN empleados ON citas.empleado_id = empleados.id
    JOIN servicios ON citas.servicio_id = servicios.id
    ORDER BY citas.fecha DESC
    """)
    data = cur.fetchall()
    cur.close()
    return data  # devuelve lista (puede ser vacía, nunca None)

# =========================
# Obtener cita por ID
# =========================
def get_cita_by_id(mysql, cita_id):
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT c.id, cl.nombre AS cliente, e.nombre AS empleado, s.nombre AS servicio,
               c.fecha, c.hora, c.estado
        FROM citas c
        JOIN clientes cl ON c.cliente_id = cl.id
        JOIN empleados e ON c.empleado_id = e.id
        JOIN servicios s ON c.servicio_id = s.id
        WHERE c.id = %s
    """, (cita_id,))
    data = cur.fetchone()
    cur.close()
    return data  # puede ser None si no existe

# =========================
# Agregar nueva cita
# =========================
def add_cita(mysql, cliente_id, empleado_id, servicio_nombre, fecha, hora, cliente_ocacional=None):
    try:
        cur = mysql.connection.cursor()

        # Buscar servicio
        cur.execute("SELECT id FROM servicios WHERE nombre = %s", (servicio_nombre,))
        row = cur.fetchone()
        if not row:
            return False, f"Servicio no encontrado: {servicio_nombre}"
        servicio_id = row[0]

        # Validar cliente
        if cliente_id and cliente_id != "1":
            if cliente_ocacional:
                return False, "Error: no puedes enviar cliente fijo y ocasional a la vez"
            cliente_nombre_manual = None
        elif cliente_id == "1" and cliente_ocacional:
            # Guardar cliente ocasional
            cur.execute("""
                INSERT INTO clientes_ocacionales (nombre, fecha_registro)
                VALUES (%s, CURDATE())
            """, (cliente_ocacional,))
            cliente_nombre_manual = cliente_ocacional
        else:
            return False, "Debes seleccionar un cliente fijo o escribir uno ocasional"

        # Verificar disponibilidad
        if not verificar_disponibilidad(mysql, empleado_id, fecha, hora, servicio_nombre):
            return False, "El empleado ya tiene una cita en ese horario"

        # Insertar cita
        cur.execute("""
            INSERT INTO citas (cliente_id, cliente_nombre_manual, empleado_id, servicio_id, fecha, hora, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (cliente_id, cliente_nombre_manual, empleado_id, servicio_id, fecha, hora, "pendiente"))

        mysql.connection.commit()
        cur.close()
        return True, None

    except Exception as e:
        print("❌ Error al guardar cita:", e)
        return False, str(e)
# =========================
# Actualizar cita
# =========================
def update_cita(mysql, cita_id, fecha, hora, estado):
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE citas
        SET fecha = %s, hora = %s, estado = %s
        WHERE id = %s
    """, (fecha, hora, estado, cita_id))
    mysql.connection.commit()
    cur.close()

# =========================
# Cancelar cita
# =========================
def cancelar_cita(mysql, cita_id):
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE citas
        SET estado = 'cancelada'
        WHERE id = %s
    """, (cita_id,))
    mysql.connection.commit()
    cur.close()

# =========================
# Verificar disponibilidad (sin choques de horarios)
# =========================
def verificar_disponibilidad(mysql, empleado_id, fecha, hora, servicio_nombre):
    # Buscar duración e ID real del servicio por nombre
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, duracion FROM servicios WHERE nombre = %s", (servicio_nombre,))
    row = cur.fetchone()
    cur.close()

    if row is None:
        print("⚠️ Servicio no encontrado:", servicio_nombre)
        return False

    servicio_id = row[0]
    duracion = row[1]

    # Calcular rango de tiempo de la cita
    hora_inicio = datetime.strptime(hora, "%H:%M")
    hora_fin = hora_inicio + timedelta(minutes=duracion)

    # Verificar si hay choque de horarios
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT COUNT(*) FROM citas c
        JOIN servicios s ON c.servicio_id = s.id
        WHERE c.empleado_id = %s AND c.fecha = %s
        AND (
            (c.hora <= %s AND ADDTIME(c.hora, SEC_TO_TIME(s.duracion*60)) > %s)
        )
    """, (empleado_id, fecha, hora_inicio.time(), hora_inicio.time()))
    resultado = cur.fetchone()[0]
    cur.close()

    print("🔍 Disponibilidad resultado:", resultado)
    return resultado == 0
