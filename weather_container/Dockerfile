FROM python:latest as builder
WORKDIR /project
COPY . /project
RUN pip3 install -r requirements.txt
#COPY flaskapp.service /etc/systemd/system
#COPY app.conf /tec/nginx/conf.d
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
#RUN gunicorn --bind 0.0.0.0:5000 wsgi:app

#FROM nginx as production





#COPY requirements.txt run.py backend_weather.py templates .env /project


#COPY app.conf /etc/nginx/conf.d
#COPY flask.service /etc/systemd/system 



#exercise 24:
#FROM python:latest
#WORKDIR /project
#COPY . /project
#RUN pip3 install -r requirements.txt
#CMD ["python3", "run.py"]













#RUN source venv/bin/activate
#RUN pip install requirements.txt
#RUN pip list

