 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
 ADD database /code/database
 ADD dht /code/dht
 ADD monitor /code/monitor
 CMD [ "python3", "./auto_terrarium.py 22 4" ]