FROM alpine:latest
# this is needed to make sure we can see the log output
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apk update 
RUN apk add python3 
RUN apk add py3-pip
RUN apk add mosquitto
RUN pip3 install paho-mqtt
COPY forwarder.py forwarder.py
CMD ["python3","forwarder.py"]

