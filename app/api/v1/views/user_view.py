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
    def post(self):
        """ endpoint for users to sign in """
        try:
            log_data = request.get_json()
            if not log_data:
                return jsonify({"status": 404, "error": "No data found"}), 404

            users = UserModels(USER_LIST, log_data)
            validate = UserValidation(log_data)
            users.check_required_present(users.required_login)
            validate.confirm_login(log_data["userlog"])
            logged_in_user = validate.correct_details[0]
            exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            token = jwt.encode(
            {"password": logged_in_user['password'], 'exp': exp}, KEY)
            return make_response(jsonify({"status": 200, "message": "logged in successfully", "token": token.decode("utf-8")}), 200)
        except TypeError:
            return make_response(jsonify({"status": 417, "error": "Expecting Login data!!"}), 417  )


