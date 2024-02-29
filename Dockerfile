FROM python:slim
WORKDIR /project/
COPY . /project
RUN pip3 install -r requirements.txt
