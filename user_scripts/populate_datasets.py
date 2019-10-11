import requests

DATA_OWNER_PORTS = {'5000':"datasets/file_0.csv",
                    '5001':"datasets/file_1.csv",
                    '5002':"datasets/file_2.csv",
                    '5003':"datasets/file_3.csv",
                    '5004':"datasets/file_4.csv",
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

