import requests

DATA_OWNER_PORTS = {'5000':"datasets/file.csv",
					'5001':"datasets/file.csv",
					'5002':"datasets/file.csv",
					'5003':"datasets/file.csv",
					'5004':"datasets/file.csv",
					}


if __name__ == '__main__':
	for do_port, file_path in DATA_OWNER_PORTS.items():
		url = "http://localhost:{}/datasets".format(do_port)
		print(url, file_path)
		with  open(file_path, 'rb') as file:
			files = {'file': file}
			response = requests.post(url,files=files)
			response.raise_for_status()
			print(response)

