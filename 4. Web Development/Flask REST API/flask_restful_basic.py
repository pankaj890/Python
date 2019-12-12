# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:33:54 2019

@author: Pankaj Goyal
"""

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello World'}
    
    def post(self):
        some_json = request.get_json()
        return {'retult': some_json}, 201
    

class Multi(Resource):
    def post(self, num):
        return {'result': num*10}
    

api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)