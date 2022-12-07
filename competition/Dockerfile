FROM ubuntu:20.04

MAINTAINER toconnor <toconnor@my.fit.edu>

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York
ENV LANG en_US.UTF-8

# apt-get installs
RUN apt-get update -y -qq
RUN apt-get install -y -qq \
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
    wget \
    python3-pip \
    ruby-dev 

RUN pip3 install --upgrade pip

RUN python3 -m pip install --no-cache-dir \
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

# install angr after dependencies met
RUN pip3 install angr angrop

# install angrop from source -- fixes "rop" import error 
RUN cd /opt/ && git clone https://github.com/angr/angrop && \
    cd angrop && pip3 install .

# install pwninit for patching bins for ctfs     
RUN wget -O /bin/pwninit https://github.com/io12/pwninit/releases/download/3.2.0/pwninit && \
    chmod +x /bin/pwninit 

# install pwndbg
RUN cd /opt/ && git clone https://github.com/pwndbg/pwndbg && \
  cd pwndbg && \
  ./setup.sh

# install one_gadget
RUN gem install one_gadget seccomp-tools && rm -rf /var/lib/gems/2.*/cache/*

# install radare
RUN wget https://github.com/radareorg/radare2/releases/download/4.4.0/radare2_4.4.0_amd64.deb && \
    dpkg -i radare2_4.4.0_amd64.deb && rm radare2_4.4.0_amd64.deb

# install zsh
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.2/zsh-in-docker.sh)" -- \
    -t crunch

# install stuff for patching binaries with libc
RUN apt-get update -qq -y && apt-get install -qq -y patchelf elfutils

WORKDIR /

# copy over libc-2.27, ld-2.27 and script to patch
COPY /libc /opt

# copy, uncompress, and patch older binaries
# COPY bins/old.tar.gz /
# RUN tar -xvzf old.tar.gz
# RUN rm -rf bins/._*
# RUN mv bins fall21-bins
# RUN python3 /opt/patch_bins.py BIN_DIR=/fall21-bins/ REPLACE
 
# copy, uncompress, and patch competition binaries
COPY bins/bins.tar.gz /
RUN tar -xvzf bins.tar.gz
RUN rm -rf bins/._*

RUN python3 /opt/patch_bins.py REPLACE

# enable core dumping
RUN ulimit -c unlimited

COPY /flag/flag.txt /flag.txt
RUN mkdir /solution
COPY execute_test/execute_test.py /execute_test.py 

# copy over solarpanth3r; remove from standard build
# COPY solution/* /aeg.py 

