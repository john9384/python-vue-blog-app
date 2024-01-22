# app/error_handling.py

from functools import wraps
from flask import jsonify

def handle_route_errors(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            # Call the original function
            return func(*args, **kwargs)
        except Exception as e:
            # Handle the specific error for this route
            response = {'error': str(e)}
            return jsonify(response), 500  # You can customize the status code

    return decorated_function
