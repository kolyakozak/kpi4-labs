import requests
import hashlib
import os

host = os.environ['HOST']
port = int(os.environ['PORT'])

url = f'http://{host}:{port}'

res = requests.get(url)

data = res.json()
try:
    md5 = hashlib.md5(data['file'].encode('utf-8')).hexdigest()
    if md5 == data['md5']:
        print('All ok')
        with open('/clientdata/file.txt', 'w') as file:
            file.write(data['file'])
    else:
        print('Checksums are not matching!')
except Exception as e:
    print(f'Error: {e}')

