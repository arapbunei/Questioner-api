import os
import datetime
import jwt
from flask import jsonify, request, make_response, Response, json,make_response
from ..models.models import USER_LIST, UserModels
from ..utils.validations import UserValidation
from flask_restful import Resource
time_now = datetime.datetime.now()


class Index(Resource):
    """ Resource for index endpoint """
    
    def get(self):
        return {'status': 200, 'message': 'Welcome to Questioner!!. A meetup platform'}, 200
class Register(Resource):
    def post(self):
        """ endpoint for user to create account """
        try:
            user_data = request.get_json()
            if not user_data:
                return jsonify({"status": 404, "error": "no userdata data!!"}), 404
            validate = UserValidation(user_data)
            users = UserModels(USER_LIST, user_data)
            users.check_required_present(users.required_signup)
            validate.valid_username()
            validate.valid_email()
            validate.valid_password()
            validate.check_signup_exists()
            new_user = users.autogen_id_and_defaults()
            users.add_admin_status()
            new_user = users.save_the_data()
            return make_response(jsonify({"status": 201, "data": new_user}), 201)
        except TypeError:
            return make_response(jsonify({"status": 417, "error": "Expecting signup data!!"}), 417)
        
class Login(Resource):
    """ Resource to login existing user """

    def post(self):
        """ Endpoint to login user """

        message = ''
        status_code = 200
        response = {}

        login_data = request.get_json()

        if not login_data:
            message = 'No data provided'
            status_code = 400

        else:
            try:
                data = UserSchema().load(login_data, partial=True)

                try:
                    username = data['username']
                    password = data['password']

                    if not db.exists('username', username):
                        status_code = 404
                        message = 'User not found'

                    else:
                        user = db.find('username', username)

                        db.checkpassword(user['password'], password)

                        access_token = create_access_token(identity=user['id'], fresh=True)
                        refresh_token = create_refresh_token(identity=True)

                        status_code = 200
                        message = 'User logged in successfully'
                        response.update({
                            'access_token': access_token,
                            'refresh_token': refresh_token,
                            'user_id': user['id']
                        })
                    
                except:
                    status_code = 400
                    message = 'Invalid credentials'

            except ValidationError as err:
                errors = err.messages

                status_code = 400
                message = 'Invalid data. Please fill all required fields'
                response.update({'errors': errors})

        response.update({'status': status_code, 'message': message})
        return response, status_code

class Tokens(Resource):
    """ Resource to refresh access token """

    @jwt_refresh_token_required
    def post(self):
        """ Endpoint to refresh user access token """

        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'status': 200, 'message': 'Token refreshed successfully', 'access_token': access_token}

class Logout(Resource):
    """ Resource to logout user """

    @jwt_required
    def post(self):
        """ Endpoint to logout user """

        user_jti = get_raw_jwt()['jti']

        RevokedTokenModel().add(user_jti)
        return {'status': 200, 'message': 'Logged out successfully'}, 200


