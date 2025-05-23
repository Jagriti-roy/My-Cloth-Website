from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt
from flask import jsonify

def roles_required(*required_roles):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()  # Get JWT claims
            user_roles = claims.get('roles', [])
            if not any(role in user_roles for role in required_roles):
                return jsonify({"message": "Forbidden: Insufficient role"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
