FROM python:3.12-slim

LABEL authors="DEpishev@alfabank.ru"

ARG TARGETARCH
COPY requirements.txt /home/app/requirements.txt
RUN pip install -r /home/app/requirements.txt
COPY main.py /home/app/main.py

ENTRYPOINT ["python3", "/home/app/main.py"]