FROM python:3.7-slim

RUN apt-get update

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY target.py /target.py

ENTRYPOINT ["python", "-u", "/target.py"]


