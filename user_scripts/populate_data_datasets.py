import requests

DATA_OWNER_PORTS = {'5000':"datasets/file.csv",
					'5001':"datasets/file.csv",
					'5002':"datasets/file.csv",
					'5003':"datasets/file.csv",
					'5004':"datasets/file.csv",
					}

files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

"""
Falta testear este script
"""
if __name__ == '__main__':
	for do_port, file in DATA_OWNER_PORTS.items():
		url = "http://localhost:{}/datasets".format(do_port)
		files = {'file': (file)}
		print(url, file)
		response = requests.post(url,file=file)
        response.raise_for_status()
        print(response)

