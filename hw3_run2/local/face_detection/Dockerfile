FROM ubuntu
  
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt install -y python3-dev python3-pip  python3-opencv vim-tiny  libopencv-dev x11-xserver-utils libcanberra-gtk-module libcanberra-gtk3-module
RUN pip3 install Cython
RUN pip3 install numpy
RUN pip3 install paho-mqtt
RUN export NO_AT_BRIDGE=0

COPY face_detection.py face_detection.py

CMD ["python3","face_detection.py"]
