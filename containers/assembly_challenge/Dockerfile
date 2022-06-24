FROM qilingframework/qiling:latest

MAINTAINER tj <toconnor@fit.edu>

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN apt-get update -y && apt-get -qq -y install git socat

WORKDIR /
RUN git clone https://github.com/qilingframework/rootfs

RUN useradd -m user

COPY flag/flag.txt /flag.txt
RUN chown root:root /flag.txt
RUN chmod 644 /flag.txt

COPY shell/* /home/user/pyshell.py
RUN chown user:user /home/user/pyshell.py
RUN chmod +x /home/user/pyshell.py

COPY start.sh /start.sh
RUN chmod 755 /start.sh

EXPOSE 31337/tcp
CMD ["./start.sh"]



