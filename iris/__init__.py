#!/usr/bin/env python3
"""
Core application logic for the central Iris Server

Shawn Chowdhury
since 2016-03-05

Built at BrickHack II
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse

import iris.parser as iris_parser

# initialize
app = Flask(__name__)
api = Api(app)


# === API Layer
req_parser = reqparse.RequestParser()
req_parser.add_argument('string', type=str, help="Natural language string to parse")


class NLPEvaluate(Resource):

    def post(self):

        args = parser.parse_args()

        try:
            response = iris_parser.evaluate(args['string'])
        except Exception as e:  # FIXME use a custom exception this is way too broad
            return {
                'error': e.args
            }, 400

        return {'data': response}, 200


# === build API endpoints
api.add_resource(NLPEvaluate, '/api/evaluate')