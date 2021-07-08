"""Block Namespace"""

from flask_restx import Namespace, Resource
from service.block import BlockService
import json
import redis

cache = redis.Redis(host='redis_db')

api = Namespace('blocks', description='Block endpoints')


@api.route('/<block>/txs/<txs>')
class BlockByBlockNumberAndTransactionIndexOrHash(Resource):
	"""Block Endpoint"""

	service = BlockService()

	def get(self, block, txs):
		"""
		Get Block By Block Number and Transaction Index or Hash

		params ->

		block -> Block Number
		txs -> Transaction index or Hash
		"""

		# Check if Block input is latest or an integer (block number)
		if block == 'latest':
			block_number = block
		elif block.isnumeric():
			block_number = hex(int(block))
		else:
			return {'error': 'Block Number should be numeric or \'latest\''}, 400

		# Check if transaction input is transaction index or transaction hash
		# If transaction index (if numeric) , hash the index
		if txs.isnumeric():
			txs = hex(int(txs))

		response = self.service.get_transaction_by_block_number_and_index(block_number, txs)

		# If API Response is not status code 200
		if not response.status_code == 200:
			return {'error': 'bad request'}, 400

		# If API returns error but returns status code 200
		if response.json().get('error'):
			return {'error': 'bad request'}, 400

		return response.json(), 200


@api.route('/<block>/')
class BlockByBlockNumber(Resource):
	"""Get Block by Block Number"""

	service = BlockService()

	def get(self, block):
		"""
		Get Method
		:param block Block Number
		"""
		if block == 'latest':
			block_number = block
		elif block.isnumeric():
			block_number = hex(int(block))
		else:
			return {'error': 'Block Number should be numeric or \'latest\''}, 400

		response = cache.get(block_number)

		if not response:

			# Get Data from Gateway
			response = self.service.get_block_by_number(block_number)

			# Cache the Data
			cache.set(block_number, json.dumps(response.json()))

			# Check if response isn't an error

			# If API Response is not status code 200
			if not response.status_code == 200:
				return {'error': 'bad request'}, 400

			# If API returns error but returns status code 200
			if response.json().get('error'):
				return {'error': 'bad request'}, 400

			# Get Json of response
			response = response.json()
		else:

			response = json.loads(response)

		return response, 200
