FROM lppier/docker-prophet

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt --upgrade

CMD ["python", "prediction.py"]