import logging
import json
from flask import Flask, request, Response
from flask_restful import Resource, Api, Headers
import os


app = Flask(__name__)
api = Api(app)

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s] %(module)s.%(funcName)s:%(lineno)s: %(message)s')

class Health(Resource):

    @staticmethod
    def get():
        logging.info("Service is healthy")
        return Response(json.dumps("Health is OK"), status=200, mimetype='application/json')

api.add_resource(Health, '/health')

logging.info('Sample Rest API started')

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5001)

