from flask import Flask
from flask_restful import Api
from controllers import Course_controller

app = Flask(__name__)

api = Api(app)




api.add_resource(Course_controller.List , '/courses')


if __name__=='__main__':
    app.run('127.0.0.1',5000,True)


