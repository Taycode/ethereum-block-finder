"""Tests for Block"""
from app import app


def test_get_block_by_number_endpoint():
	"""Test Get Block By Number API Endpoint"""
	client = app.test_client()
	number_response = client.get('/block/1/')
	latest_response = client.get('/block/latest/')
	assert number_response.status_code == 200
	assert latest_response.status_code == 200


def test_get_transaction_by_number_and_index_endpoint():
	"""Test Get Block By Number and Index"""
	client = app.test_client()
	response = client.get('/block/1/txs/1/')
	assert response.status_code == 200
