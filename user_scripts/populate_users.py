import uuid
import requests
from web3 import Web3
#
ETH_URL = "http://127.0.0.1:8545"

DATA_OWNER_PORTS = ['5000',
                    '5001',
                    '5002',
                    '5003',
                    '5004',
                    ]


def build_new_user_data(address):
    return {
        'name': 'User {}'.format(address),
        'email': '{}@deltaml.com'.format(str(uuid.uuid1())),
        'token': '1234567890'
    }


def build_register_user_data(address):
    return {
        'address': address
    }


def create_data_owners(available_accounts):
    print("Init Data owner creation")    
    for do_port in DATA_OWNER_PORTS:
        account = available_accounts.pop()
        data = build_new_user_data(account)
        url = "http://localhost:{}/users".format(do_port)
        print(url, data)
        create_response = requests.post(url, json=data)
        create_response.raise_for_status()
        json_response = create_response.json()
        print(json_response)
        register_url = "http://localhost:{}/users/{}/register".format(do_port, json_response["id"])
        print(register_url)
        register_response = requests.post(register_url, json=build_register_user_data(account))
        register_response.raise_for_status()
        print(register_response.json())

    print("Finish Data owner creation")    


def create_new_model_buyer(account):
    print("Init Model buyer creation")
    data = build_new_user_data(account)
    url = "http://localhost:9090/users"
    print(url, data)
    create_response = requests.post(url, json=data)
    create_response.raise_for_status()
    json_response = create_response.json()
    print(json_response)
    register_url = "http://localhost:9090/users/{}/address".format(json_response["id"])
    print(register_url)
    register_response = requests.post(register_url, json=build_register_user_data(account))
    register_response.raise_for_status()
    print(register_response.json())
    print("Finish Model buyer creation")


def set_fa_account_address(avaiables_accounts):
    print("Init update FA account address")
    address_url = "http://localhost:8080/federated-aggregator"
    account = avaiables_accounts.pop()
    print(address_url, account)
    register_response = requests.patch(address_url, json=build_register_user_data(account))
    register_response.raise_for_status()
    print(register_response.json())
    print("Finish update FA account address")
    return account


if __name__ == '__main__':
    w3 = Web3(Web3.HTTPProvider(ETH_URL)).eth
    fa_account = set_fa_account_address(w3.accounts)
    available_accounts = [account for account in w3.accounts if account != fa_account]
    create_data_owners(available_accounts)

