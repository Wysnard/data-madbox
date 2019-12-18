FROM python:3

ADD . /app

WORKDIR /app

RUN apt-get -y update  && apt-get install -y
RUN pip install -r requirements.txt --upgrade

CMD ["python", "injector.py"]