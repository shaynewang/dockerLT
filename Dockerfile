FROM ubuntu
MAINTAINER Shayne Wang shaynexwang@gmail.com
RUN apt-get update && apt-get install -y sudo
RUN apt-get install -y python git
RUN git clone https://github.com/shaynewnag/dockerLT
RUN cd dockerLT
RUN python pytest.py
