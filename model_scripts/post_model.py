import requests
import json

FILE_PATH = 'model.json' 
MODEL_BUYER_URL = 'http://localhost:9090/models' 

if __name__ == '__main__':

	with open(FILE_PATH) as json_file:
		data = json.load(json_file)
		model_response = requests.post(MODEL_BUYER_URL, json=data)
		model_response.raise_for_status()
		print(model_response.json())