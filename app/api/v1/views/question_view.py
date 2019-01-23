from flask import jsonify, request, make_response
from ..schemas.question_schema import QuestionSchema
from ..models.question_model import Question as QuestionModel
from ..models.meetup_model import Meetup
from marshmallow import ValidationError
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from flask_restful import Resource

db = QuestionModel()
meetups_db = Meetup()

class Question(Resource):
    """ Resource for question endpoints """

    @jwt_required
    def post(self):
        """ Endpoint to post question """

        message = ''
        status_code = 200
        response = {}

        meetup_data = request.get_json()

        if not meetup_data:
            message = 'No data provided'
            status_code = 400

        else:
            try:
                meetup = meetup_data['meetup_id']
                
                if not meetups_db.exists('id', meetup):
                    message = 'Meetup not found'
                    status_code = 404

                else:
                    try:
                        data = QuestionSchema().load(meetup_data)

                        data['user_id'] = get_jwt_identity()
                        question = db.save(data)
                        result = QuestionSchema().dump(question)

                        status_code = 201
                        message = 'Question posted successfully'
                        response.update({'data': result})

                    except ValidationError as err:
                        errors = err.messages

                        status_code = 400
                        message = 'Invalid data. Please fill all required fields'
                        response.update({'errors': errors})

            except:
                message = 'Meetup not found'
                status_code = 404

        response.update({'status': status_code, 'message': message})
        return response, status_code

