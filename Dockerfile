FROM python:latest

RUN apt-get update && apt-get install -y git vim pip\
    && pip install --upgrade pip

COPY requirements.txt .
COPY .gitconfig /root/
COPY .ssh /root/.ssh

RUN pip install -r requirements.txt

WORKDIR /root/../home/