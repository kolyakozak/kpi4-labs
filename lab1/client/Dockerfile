FROM python:3.8.12-alpine

RUN mkdir -p /home/app
RUN mkdir -p /clientdata

ADD ./client.py /home/app/
ADD ./requirements.txt /home/app/

RUN pip install -r /home/app/requirements.txt

ENTRYPOINT [ "python", "/home/app/client.py" ]