"""Block Service"""
import requests
import json


class BlockService:
	"""Block Service Module"""
	base_url = 'https://cloudflare-eth.com'

	def get_block_by_number(self, block_number):
		"""Gets block number by number"""
		data = {
			'jsonrpc': '2.0',
			'method': 'eth_getBlockByNumber',
			'params': [block_number, True],
			'id': 1
		}
		response = requests.post(self.base_url, json.dumps(data))
		return response.json()

	def get_transaction_by_hash(self, transaction_hash):
		"""Gets Transaction by hash"""
		data = {
			'jsonrpc': '2.0',
			'method': 'eth_getTransactionByHash',
			'params': [transaction_hash],
			'id': 1
		}
		response = requests.post(self.base_url, json.dumps(data))
		return response.json()

	def get_transaction_by_block_number_and_index(self, block_number, index):
		"""Gets Transaction by Block number and index"""
		data = {
			'jsonrpc': '2.0',
			'method': 'eth_getTransactionByBlockNumberAndIndex',
			'params': [block_number, index],
			'id': 1
		}
		response = requests.post(self.base_url, json.dumps(data))
		return response.json()
