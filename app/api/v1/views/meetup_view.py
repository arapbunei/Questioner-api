from flask import jsonify, request, make_response
from ..schemas.meetup_schema import MeetupSchema
from ..models.meetup_model import Meetup as MeetupModel
from marshmallow import ValidationError
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from flask_restful import Resource

db = MeetupModel()

class Meetups(Resource):
    """ Resource for meetup endpoints """

    @jwt_required
    def post(self):
        """ Endpoint to create meetup """

        message = ''
        status_code = 200
        response = {}

        json_data = request.get_json()

        if not json_data:
            message = 'No data provided'
            status_code = 400

        else:
            try:
                data = MeetupSchema().load(json_data)

                data['user_id'] = get_jwt_identity()
                new_meetup = db.save(data)
                result = MeetupSchema().dump(new_meetup)

                status_code = 201
                message = 'Meetup created successfully'

            except ValidationError as err:
                errors = err.messages

                status_code = 400
                message = 'Invalid data. Please fill all required fields'
                response.update({'errors': errors})

        response.update({'status': status_code, 'message': message})
        return response, status_code

    def get(self):
        """ Endpoint to fetch all meetups """

        meetups = db.all()
        result = MeetupSchema(many=True).dump(meetups)
        return {'status':200, 'data':result}, 200

