"""Controllers"""

from flask_restx import Api
from .block import api as block_api

api = Api(title='ETH Finder App', description='Find ETH Blocks', doc='/docs/')
api.add_namespace(block_api, '/block')
