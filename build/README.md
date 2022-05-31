# Build Environment

To prevent unintended and inappropriate student collaboration, we randomly generate binaries for each iteration of the course. The following build environment allows us to generate randomized unique binaries for [bomb-lab](templates/bomb-lab), [math-chals](templates/math-chals), [angry-chals](templates/angry-chals), and [arm-chals](templates/arm-chals) labs, as well as our [competition](templates/competition). Each binary is developed from a ``jinja2`` template. 

We've also included a [Dockerfile](Dockerfile) to simplify building challenges. Simply build the docker image, and map the absolute path to the ``bin`` directory to ``/root/workspace/bin`` when starting the container. You may generate binaries for either ``[bomb-lab | math-lab | arm-lab | angry-lab | competition | all]``

```
$ docker build -t build-env .
<..snipped..>

$ docker run -it -v /absolute/path/to/bin:/root/workspace/bin build-env python3 build.py bomb-lab
[+] Randomly generating and compiling bomblab.

$ ls -l bin/*
-rwxr-xr-x  1 tj  staff  16880 May 27 11:43 bin/bomblab

$ file bin/*
bin/bomblab: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=dacea857fe2f4db9654ca5ab609f709fc107a9c3, for GNU/Linux 3.2.0, not stripped

$ docker run -it -v /absolute/path/to/bin:/root/workspace/bin build-env python3 build.py arm-lab
[+] Randomly generating and compiling arm challenges

$ ls -l bin/*
-rwxr-xr-x  1 tj  staff   5592 May 27 11:45 bin/arm-100
-rwxr-xr-x  1 tj  staff   5588 May 27 11:45 bin/arm-200
-rwxr-xr-x  1 tj  staff   5588 May 27 11:45 bin/arm-300
-rwxr-xr-x  1 tj  staff   8792 May 27 11:45 bin/arm-400
-rwxr-xr-x  1 tj  staff  16880 May 27 11:43 bin/bomblab

$ file bin/arm-100 
bin/arm-100: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-armhf.so.3, BuildID[sha1]=5f3bc9cd48703c125f4b7f47b43a6cefbdb455a3, for GNU/Linux 3.2.0, stripped

```
