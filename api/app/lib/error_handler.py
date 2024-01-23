# app/error_handling.py

from functools import wraps
from flask import jsonify

def handle_route_errors(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(str(e))
            response = {'error': str(e), 'status_code': 500}
            return jsonify(response)

    return decorated_function
