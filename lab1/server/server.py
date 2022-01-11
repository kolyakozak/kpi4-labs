import random
import string
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import hashlib
import os

file_name = '/serverdata/file.txt'
file_size = 1024 # in bytes
PORT = int(os.environ['PORT'])

random_chars = ''.join([random.choice(string.ascii_letters) for i in range(file_size)])


with open(file_name, 'w') as f:
    f.write(random_chars)


app = FastAPI(PORT=PORT)

@app.get("/")
def index():
    with open(file_name, 'r') as f:
        file = f.read()
        md5 = hashlib.md5(file.encode('utf-8')).hexdigest()
        return {'file': file, 'md5': md5}

if __name__ == "__main__":
    uvicorn.run(app, port=PORT)

