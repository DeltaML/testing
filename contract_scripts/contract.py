import argparse
import requests

parser = argparse.ArgumentParser(description='Update deltaml contract address on model buyer and fed agg')
parser.add_argument('address', metavar='N', type=str, help='an integer for the accumulator')


def update_contract_address(address):
    print("Init contract address update")

    contract_url_template = "http://localhost:{}/contract"
    ports = ["8080", "9090"]
    for port in ports:
        url = contract_url_template.format(port)
        register_response = requests.patch(url, json={
            'address': address
        })
        register_response.raise_for_status()
        print(register_response.json())

    print("Finish contract address update")


if __name__ == '__main__':
    args = parser.parse_args()
    print(args.address)
    update_contract_address(args.address)
