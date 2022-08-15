FROM kalilinux/kali-rolling

MAINTAINER toconnor <toconnor@my.fit.edu>

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

# apt-get installs
RUN apt-get update -y
RUN apt-get install -y \
    g++ \
    gcc \
    gcc-multilib \
    gdb \
    gdb-multiarch \
    git \
    locales \
    make \
    man \
    nano \
    nasm \
    pkg-config \
    tmux \
    wget 

RUN apt-get install -y python3-pip
RUN apt-get install -y ruby

# python3 pip installs
RUN python3 -m pip install --no-cache-dir \
    angr \
    angrop \
    autopep8 \
    capstone \
    colorama \
    cython \
    keystone-engine \
    pefile \
    pwntools \
    qiling \
    r2pipe \
    ropgadget \
    ropper \
    sudo \
    unicorn \
    z3-solver 

# install angrop from source -- fixes "rop" import error
RUN cd /opt/ && git clone https://github.com/angr/angrop && \
    cd angrop && pip3 install . 

# install pwndbg
RUN cd /opt/ && git clone https://github.com/pwndbg/pwndbg && \
  cd pwndbg && \
  ./setup.sh

RUN apt-get install -y ruby-dev
# install one_gadget
RUN gem install one_gadget seccomp-tools && rm -rf /var/lib/gems/2.*/cache/*

# install radare
RUN wget https://github.com/radareorg/radare2/releases/download/4.4.0/radare2_4.4.0_amd64.deb && \
    dpkg -i radare2_4.4.0_amd64.deb && rm radare2_4.4.0_amd64.deb

# install libc database
RUN git clone --depth 1 https://github.com/niklasb/libc-database.git libc-database && \

# libc database
RUN cd /opt/ && \
    git clone --depth 1 https://github.com/niklasb/libc-database.git libc-database && \
    cd libc-database && \
    ./get ubuntu debian || echo "/libc-database/" > ~/.libcdb_path

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8 

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.2/zsh-in-docker.sh)" -- \
    -t crunch

WORKDIR /

COPY bins/bins.tar.gz /bins.tar.gz
RUN tar -xvzf /bins.tar.gz
RUN rm -rf /bins/._*
COPY solution/* /aeg.py 
COPY /flag/flag.txt /flag.txt
COPY execute_test/execute_test.py /execute_test.py 

