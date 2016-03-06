#!/usr/bin/env python3
"""
Core application logic for the central Iris Server

Shawn Chowdhury
since 2016-03-05

Built at BrickHack II
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse


# initialize
app = Flask(__name__)
api = Api(app)


# === API Layer
parser = reqparse.RequestParser()
parser.add_argument('string', type=str, help="Natural language string to parse")


class NLPEvaluate(Resource):

    def post(self):

        args = parser.parse_args()




        return {'data': 'fooBar'}, 200


# === build API endpoints
api.add_resource(NLPEvaluate, '/api/evaluate')