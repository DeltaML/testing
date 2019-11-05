import uuid
import requests
from web3 import Web3

ETH_URL = "http://127.0.0.1:8545"

def get_balances(w3, accounts):
    print("Account Balances")
    for account in accounts:
        balance = w3.fromWei(int(w3.eth.getBalance(account)), 'ether')
        print("Account: {} - Balance: {} Ether".format(account, balance))
        
if __name__ == '__main__':
    w3 = Web3(Web3.HTTPProvider(ETH_URL))
    get_balances(w3, w3.eth.accounts)

