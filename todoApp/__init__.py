from flask import Flask
from flask_restplus import Api

application = Flask(__name__)
api = Api(application, version='1.0', title='Todo-List API',
    description='A Todo List API',
)

from todoApp import views