from flask_restplus import Namespace, Resource, fields

api = Namespace('users', description='User related operations')

user = api.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'name': fields.String(required=True, description='The user name'),
})

USERS = [
    {'id': 'medor', 'name': 'Medor'},
    {'id': 'medor2', 'name': 'Medor2'}
]


@api.route('/')
class DogList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        '''List all users'''
        return USERS


@api.route('/<id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, id):
        '''Fetch a User given its identifier'''
        for user in USERS:
            if user['id'] == id:
                return user
        api.abort(404)
