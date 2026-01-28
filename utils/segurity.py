from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    """Decorador para exigir que el usuario esté logueado"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Debes iniciar sesión para acceder", "error")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function


def role_required(*role):
    """Decorador para exigir un rol específico"""
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if "usuario_id" not in session:
                flash("Debes iniciar sesión", "error")
                return redirect(url_for("auth.login"))
            
            user_role = session.get("usuario_rol")
            
            # Verificar si el rol del usuario está en los roles permitidos
            if user_role not in role:
                flash("No tienes permisos para acceder a esta sección", "error")
                return redirect(url_for("index"))
            return f(*args, **kwargs)
        return decorated_function
    return wrapper
