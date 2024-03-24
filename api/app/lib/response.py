from flask import jsonify

OK = 200
CREATED = 201
BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
INTERNAL_ERROR = 500
UNPROCESSABLE_ENTITY = 422

class ApiResponse:
  def __init__(self, message, content):
    pass

  def send(self):
    pass

class SuccessResponse:
  def __init__(self, message, content, statusCode=OK):
    self.statusCode = OK 
    self.message = message
    self.content = content

  def send(self):
    return jsonify({'success': True, 'statusCode': self.statusCode, 'message': self.message, 'content': self.content})


class BadRequestResponse:
  def __init__(self, message, content, statusCode=BAD_REQUEST):
    self.statusCode = statusCode
    self.message = message
    self.content = content

  def send(self):
    return jsonify({'success': False, 'statusCode': self.statusCode, 'message': self.message, 'content': self.content})