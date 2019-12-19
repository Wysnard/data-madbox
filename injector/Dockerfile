FROM python:3

ADD . /app

WORKDIR /app

RUN apt-get -y update  && apt-get install -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "injector.py"]