# syntax=docker/dockerfile:1

FROM python:alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/ .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-p", "80"]
