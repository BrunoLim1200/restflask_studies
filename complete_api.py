#Here, I just pratice and keep notes to a complete api, using GET, PUT, POST and DELETE methods

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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
@app.route('/dev/<int:id>/', methods=['GET', 'PUT','DELETE'])
def listDevelopers(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            message = 'This developer ID {} dosent exist'.format(id)
            response = {'status':'error', 'message':message}
        except Exception:
            message = 'Unknow error. Contact the administrator.'
            response = {'status':'error', 'message':message}
        return jsonify(response)
    elif request.method == 'PUT':
        info = json.loads(request.data)
        developers[id] = info
        return jsonify(info)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status':'success', 'message':'Deleted'})

# List all developers and include a new developer
@app.route('/dev/', methods=['POST', 'GET'])
def devInclude():
    if request.method == 'POST':
        dados = json.loads(request.data)
        position = len(developers)
        dados['id'] = position
        developers.append(dados)
        return jsonify(developers[position])
    elif request.method == 'GET':
        return jsonify(developers)

if __name__ == '__main__':
    app.run(debug=True)