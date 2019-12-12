# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:55:19 2019

@author: Pankaj Goyal
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        some_json = request.get_json()
        return jsonify({'You_Sent': some_json}), 201
    else:
        return jsonify({'about': 'Hello Pankaj'})
    
    
@app.route('/multiply/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'Result : ': num*10})


if __name__ == '__main__':
    app.run(debug=True)
