from flask_restplus import Namespace, Resource, fields

api = Namespace('merchants', description='Merchant related operations')

merchant = api.model('Merchant', {
    'id': fields.String(required=True, description='The Merchant identifier'),
    'name': fields.String(required=True, description='The Merchant name'),
})

MERCHANTS = [
    {'id': 'felix', 'name': 'Felix'},
    {'id': 'felix2', 'name': 'Felix2'}
]


@api.route('/')
class MerchantList(Resource):
    @api.doc('list_all_merchants')
    @api.marshal_list_with(merchant)
    def get(self):
        '''List all merchants'''
        return MERCHANTS


@api.route('/<id>')
@api.param('id', 'The merchant identifier')
@api.response(404, 'merchant not found')
class Merchant(Resource):
    @api.doc('get_one_merchant')
    @api.marshal_with(merchant)
    def get(self, id):
        '''Fetch a merchant given its identifier'''
        for merchant in MERCHANTS:
            if merchant['id'] == id:
                return merchant
        api.abort(404)


