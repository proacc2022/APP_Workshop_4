from flask_restful import reqparse, Resource
from flask import make_response   # returns an HTML response
from services.RiderService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', type=str)
post_parser.add_argument('premium', type=bool, default=False)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('premium', type=bool, default=False)

headers = {'Content-Type': 'application/json'}


class RiderResource(Resource):
    def get(self, rider_id=None):
        response = get_rider(rider_id)
        return make_response(response.to_json(), 200, headers)

    def post(self):
        args = post_parser.parse_args()
        response = create_rider(args.name, args.premium)
        return make_response(response.to_json(), 200, headers)

    def patch(self, rider_id=None):
        if rider_id is not None:
            args = patch_parser.parse_args()
            response = update_rider(rider_id, args.premium)
            return make_response(response.to_json(), 200, headers)
        return make_response("Error Message", 400, headers)
