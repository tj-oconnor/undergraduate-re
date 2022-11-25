FROM ubuntu:18.04

MAINTAINER tj <toconnor@fit.edu>

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

# install python3 and pip3
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip \
    gcc-arm-linux-gnueabi \
    gcc-arm-linux-gnueabihf

# install python3 libraries
RUN python3 -m pip install --no-cache-dir \
    jinja2 pyfiglet randomname

# setup environment
RUN mkdir -p /root/workspace
WORKDIR /root/workspace 
RUN mkdir -p /root/workspace/src
COPY build.py /root/workspace/build.py
COPY helper_funcs.py /root/workspace/helper_funcs.py
COPY templates /root/workspace/templates

