import os

# =========================
# Configuración de Flask
# =========================
SECRET_KEY = os.environ.get("SECRET_KEY", "clave_secreta_para_sesiones")

# =========================
# Configuración de MySQL
# =========================
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_USER = os.environ.get("MYSQL_USER", "Jereck")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "Jereck22User@")
MYSQL_DB = os.environ.get("MYSQL_DB", "bwa_db")

# =========================
# Configuración de correo (Flask-Mail)
# =========================
MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "tu_correo@gmail.com")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "tu_password_correo")
MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER", "tu_correo@gmail.com")
MAIL_SUPPRESS_SEND = False  # Cambiar a True en entorno de desarrollo para evitar enviar correos reales
MAIL_DEBUG = os.environ.get("MAIL_DEBUG", True)