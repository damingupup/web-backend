from flask_restplus import Api

from .user import api as user_api
from .merchant import api as merchant_api
from .auth import api as auth_api

api = Api(
    title='Chines BBB API',
    version='1.0',
    description='API (Alpha version)',
)

api.add_namespace(user_api)
api.add_namespace(merchant_api)
api.add_namespace(auth_api)
