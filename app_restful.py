#Here, I just pratice and keep notes to a complete api, using Flask-RESTful

from flask import Flask, request
from flask_restful import Resource, Api
from skills import listSkills
import json

app = Flask(__name__)
api = Api(app)

developers = [
    {
        'id':'0',
        'name':'Rafael',
        'skills':['Python', 'Flask']
     },
    {
        'id':'1',
        'name': 'Bruno',
        'skills': ['Python', 'Java']
     },
]

# get a developer per ID, also delete
class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            message = 'This developer ID {} dosent exist'.format(id)
            response = {'status': 'error', 'message': message}
        except Exception:
            message = 'Unknow error. Contact the administrator.'
            response = {'status': 'error', 'message': message}
        return response

    def put(self):
        info = json.loads(request.data)
        developers[id] = info
        return info

    def delete(self):
        developers.pop(id)
        return {'status': 'success', 'message': 'Deleted'}

# List all developers and include a new developer
class listDevelopers (Resource):
    def get(self):
        return developers
    def post(self):
        dados = json.loads(request.data)
        position = len(developers)
        dados['id'] = position
        developers.append(dados)
        return developers[position]

api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(listDevelopers, '/dev/')
api.add_resource(listSkills, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)