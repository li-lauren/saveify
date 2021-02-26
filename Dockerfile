FROM python:3.6-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
# RUN /bin/bash -c "source /app/secrets.sh"

CMD [ "python3", "server.py"]