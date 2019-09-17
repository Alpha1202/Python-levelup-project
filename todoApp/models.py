from flask_restplus import fields
from todoApp import api


todo = api.model('Todo', {
    'id': fields.Integer('ID', readonly=True, description='A todo unique identifier'),
    'title': fields.String('TITLE', required=True, description='A todo title'),
    'description': fields.String('DESCRIPTION', required=True, description='A todo description')
})