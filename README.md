<h1 align="center">💇‍♀️ BeautyAgenda Web</h1>
<p align="center"><em>Gestor de citas y administración para salones de belleza ✨</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python"/>
  <img src="https://img.shields.io/badge/Flask-Framework-lightgrey?logo=flask"/>
  <img src="https://img.shields.io/badge/MySQL-Database-blue?logo=mysql"/>
  <img src="https://img.shields.io/badge/Semantic%20UI-Frontend-teal?logo=semantic-ui"/>
  <img src="https://img.shields.io/badge/Proyecto-En%20Desarrollo-yellow"/>
</p>

---

## ✨ Descripción del Proyecto

**BeautyAgenda Web** es una aplicación web desarrollada con **Flask** y **MySQL**, que permite administrar clientes, empleados, servicios y citas de un salón de belleza de forma intuitiva.  

Su objetivo es brindar una solución práctica para salones pequeños o medianos que deseen optimizar la gestión de citas y la comunicación con sus clientes, manteniendo una interfaz simple, moderna y funcional.

Entre sus principales características se incluyen:
- Registro, edición y eliminación de clientes y empleados.  
- Programación, modificación y cancelación de citas.  
- Asociación de citas con servicios disponibles en el salón.  
- Módulo de correos con recordatorios automáticos y mensajes institucionales.  
- Plantillas dinámicas para campañas promocionales.  
- Panel de control con historial y notificaciones.  
- Interfaz moderna construida con **Semantic UI**.

---

## ⚙️ Tecnologías Utilizadas

El proyecto fue desarrollado utilizando las siguientes herramientas y tecnologías:

| 💻 Categoría            | 🧩 Tecnologías |
|--------------------------|----------------|
| **Backend**              | 🐍 Flask (Python), 🗄️ MySQL |
| **Frontend**             | 🎨 HTML5, CSS3, 💠 Semantic UI, ⚡ Font Awesome |
| **Servidor local**       | ⚙️ XAMPP |
| **Control de versiones** | 🌿 Git & 🐙 GitHub |
| **Entorno de desarrollo**| 🧠 Visual Studio Code |
| **Base de datos**        | 🧾 MySQL Workbench |

---

## 🗂️ Estructura del proyecto

```bash
BeautyAgendaWeb/
│
├── app.py              # 🧠 Archivo principal de la aplicación Flask
├── config.py           # ⚙️ Configuración de la aplicación (MySQL, claves, etc.)
├── requirements.txt    # 📦 Dependencias del proyecto
│
├── extensions.py       # 🔌 Inicialización de extensiones (MySQL, etc.)
│
├── static/             # 🎨 Archivos estáticos (CSS, JS, imágenes)
│   ├── css/
│   ├── js/
│   └── img/
│
├── templates/          # 🧩 Plantillas HTML (vistas del sistema)
│   ├── base_2.html
│   ├── index.html
│   └── s_correo/       # 📧 Módulo de correos
│       ├── recordatorios.html
│       ├── mensajes_globales.html
│       ├── plantillas.html
│       └── historial_correos.html
│
├── models/             # 🗄️ Modelos de datos
│   ├── citas.py
│   ├── clientes.py
│   ├── empleados.py
│   ├── servicios.py
│   └── correo.py
│
├── routes/             # 🚏 Blueprints de rutas
│   ├── citas.py
│   ├── clientes.py
│   ├── empleados.py
│   ├── servicios.py
│   ├── auth.py
│   ├── crear_usuario.py
│   ├── prueba.py
│   └── correo.py
│
├── docs/               # 📚 Documentación y scripts SQL
│   └── sql/
│       ├── schema.sql
│       └── correo.sql
│
└── README.md           # 📘 Documentación principal del proyecto
```

---

## 🚀 Instalación y Ejecución

Sigue estos pasos para clonar y ejecutar el proyecto en tu entorno local:

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/Hernandez2299/BeautyAgendaWeb.git
cd beautyagenda-web
```
### 2️⃣ Crear y activar un entorno virtual
En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```
En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```
### 4️⃣ Configurar la base de datos
Asegúrate de tener un servidor MySQL en ejecución y crea una base de datos llamada:
```sql
CREATE DATABASE beautyagenda;
Luego, actualiza las credenciales en el archivo config.py o app.py:
```
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'beautyagenda'
```
###5️⃣ Ejecutar la aplicación

```bash
python app.py
La aplicación estará disponible en tu navegador en: 👉 http://127.0.0.1:5000/
```

---

## 🚀 Próximas Mejoras

✨ Estas son algunas ideas que marcarán la evolución de **BeautyAgenda Web**:

- [ ] 📧 Sistema avanzado de **notificaciones por correo** con plantillas personalizadas  
- [ ] 📱 Interfaz **responsive** optimizada para móviles y tablets  
- [ ] 🔍 **Filtros inteligentes** para citas, clientes y servicios  
- [ ] 📄 Exportación de **reportes en PDF/Excel** para análisis administrativo  
- [ ] 🔐 Autenticación con **Google / Facebook** para mayor comodidad  
- [ ] 📊 Panel de **estadísticas visuales** con gráficas dinámicas  
- [ ] ⚡ Mejoras de **rendimiento y velocidad de carga**  
- [ ] 🌙 Implementación de **modo oscuro** para una experiencia moderna  

---

## 👨‍💻 Autor

<h3 align="center">Jeremy Hernández Mera</h3>
<p align="center"><strong>JJ</strong> — Mi identidad y mi sello personal</p>

💡 *“El código no solo resuelve problemas, también refleja la visión y estilo de quien lo escribe.”*  

✨ Proyecto desarrollado como parte del portafolio académico en la **Universidad de Guayaquil** ✨  

---

## 📄 Licencia

Este proyecto se publica con fines educativos y de portafolio.  
Eres libre de revisarlo, mejorarlo o inspirarte en su estructura, siempre reconociendo la autoría original.
---

## 🙌 Referencias e Inspiración

Este proyecto fue desarrollado íntegramente por **Jeremy Hernández Mera**.  
El código, la arquitectura y las funcionalidades fueron creadas desde cero, pero la presentación del README.md tomó inspiración en el proyecto:

- [Gestor de Citas Médicas – iparra-sys](https://github.com/iparra-sys/gestor-citas-medicas)

💡 Reconozco su aporte como referencia visual y de estilo, aunque toda la implementación técnica es propia.

