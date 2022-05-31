FROM ubuntu:latest

MAINTAINER tj <toconnor@fit.edu>

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN apt-get -qq update && apt-get -qq -y upgrade
RUN apt-get install -qq -y xinetd gcc build-essential cmake git libjson-c-dev libwebsockets-dev git gdb 

WORKDIR /

RUN useradd -m user

COPY flag/flag*.txt /home/user/.
RUN chown root:root /home/user/flag*
RUN chmod 644 /home/user/flag*

COPY bin/* /home/user/chal
RUN chown user:user /home/user/chal
RUN chmod +x /home/user/chal

RUN git clone https://github.com/tsl0922/ttyd.git
RUN mkdir /ttyd/build
RUN cd /ttyd/build/ && cmake .. && make && make install 
 
COPY start.sh /start.sh
RUN chmod 755 /start.sh

WORKDIR /home/user
EXPOSE 7681/tcp

CMD ["/start.sh"]
