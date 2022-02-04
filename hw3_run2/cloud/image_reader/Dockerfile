FROM ubuntu
  
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt install -y python3-dev python3-pip  python3-opencv vim-tiny  libopencv-dev x11-xserver-utils libcanberra-gtk-module libcanberra-gtk3-module
RUN pip3 install Cython
RUN pip3 install numpy
RUN pip3 install paho-mqtt
RUN pip3 install boto3
RUN pip3 install DateTime
COPY aws_creds.py aws_creds.py
COPY image_reader.py image_reader.py
CMD python3 image_reader.py
