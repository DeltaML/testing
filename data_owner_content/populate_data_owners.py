import requests
from web3 import Web3

ETH_URL = "http://127.0.0.1:7545"
CONTRACT_ADDRESS = '0xe530004720c827ead929fE0B2F01692197cfa5D2'
FEDERATED_AGGREGATOR_ADDRESS = "0x96023Cd56401b6dDa5cC839c92A3534e793CfC92"

DATA_OWNER_PORTS = ['5000',
					'5001',
					'5002',
					'5003',
					'5004',
					]

def build_new_data_owner_data(address):
	return {
		'name': 'Data Owner {}'.format(address),
		'email': '{}@deltaml.com'.format(address),
		'token': '1234567890',
		'address': address
	}

def build_register_data_owner_data(address):
	return {
		'address': address
	}


if __name__ == '__main__':
	w3 = Web3(Web3.HTTPProvider(ETH_URL)).eth
	print(w3.accounts)
	data_owners_available_accounts = [account for account in w3.accounts if account != FEDERATED_AGGREGATOR_ADDRESS]
	for do_port in DATA_OWNER_PORTS:
		account = data_owners_available_accounts.pop()
		data = build_new_data_owner_data(account)
		url = "http://localhost:{}/users".format(do_port)
		print(build_new_data_owner_data(account))
		print(url)
		create_response = requests.post(url, json=data)
		create_response.raise_for_status()
		json_response = create_response.json()
		print(json_response)
		register_url = "http://localhost:{}/users/{}/register".format(do_port, json_response["id"])
		print(register_url)
		register_response = requests.post(register_url, json=build_register_data_owner_data(account))
		register_response.raise_for_status()
		print(register_response.json())

