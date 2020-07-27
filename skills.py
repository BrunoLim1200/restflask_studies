from flask_restful import Resource

skillsList = ['Python', 'Java', 'Flask', 'PHP']
class listSkills(Resource):
    def get(self):
        return skillsList