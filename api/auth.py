from flask_restplus import Namespace, Resource, fields
from flask import request, session

api = Namespace('auth', description='Authentication related operations')

parser = api.parser()
# parser.add_argument('username', type=str, required=True, help='The username', location='form')


credential = api.model('Login', {
    'username': fields.String(required=True, description='The user username'),
    'password': fields.String(required=True, description='The user password'),
})

@api.route('/login')
class LoginAPI(Resource):
    @api.doc('to login')
    @api.expect(credential, validate=True)
    def post(self):
        if not session.get('logged_in'):
            post_data = request.json
            print(post_data)
            session['logged_in'] = True
            session['username'] = 'username1'



@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        session['logged_in'] = False
