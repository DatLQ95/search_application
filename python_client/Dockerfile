FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY client.py client.py
ENV SERVER_IP 192.168.2.93
CMD [ "python3", "client.py", "--host=0.0.0.0"]