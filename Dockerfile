FROM python:3.9.4

COPY requirements.txt /requirements.txt

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r /requirements.txt

COPY . /image_app

ENV PYTHONPATH=/image_app
WORKDIR /image_app

EXPOSE 8080

CMD python -m main