FROM python:3.6.9
ADD . /server
WORKDIR /server
RUN pip install -r requirements.txt
EXPOSE 5000
