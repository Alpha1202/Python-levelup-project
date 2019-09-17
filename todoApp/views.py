from todoApp.models import todo
from todoApp import api
from flask_restplus import Resource

todos = [
    {
        'id' : 1, 
        'title' : 'create new todo', 
        'description' : 'This is the description of the first todo'
    }, 
    {
        'id' : 2, 
        'title' : 'create another todo', 
        'description' : 'This is the description of the second todo'
    },
    {
        'id' : 3, 
        'title' : 'Third todo', 
        'description' : 'This is the description of the third todo'
    },
    {
        'id' : 4, 
        'title' : 'Fourth todo', 
        'description' : 'This is the description of the third todo'
    },
    {
        'id' : 5, 
        'title' : 'Fifth todo', 
        'description' : 'This is the description of the third todo'
    }
]

@api.route('/to-do')
class Todo(Resource):

    @api.marshal_with(todo, envelope='AllTodos')
    def get(self):
        return todos