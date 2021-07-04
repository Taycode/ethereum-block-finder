"""Block Namespace"""

from flask_restx import Namespace, Resource
from service.block import BlockService

api = Namespace('blocks', description='Block endpoints')


@api.route('/<block>/txs/<txs>')
class BlockByBlockNumberAndTransactionIndexOrHash(Resource):
	"""Block Endpoint"""

	service = BlockService()

	def get(self, block, txs):
		"""Get Method"""
		response = self.service.get_transaction_by_block_number_and_index(hex(block), txs)
		return response


@api.route('/<block>/')
class BlockByBlockNumber(Resource):
	"""Get Block by Block Number"""

	service = BlockService()

	def get(self, block):
		"""Get Method"""
		response = self.service.get_block_by_number(hex(int(block)))
		return response
