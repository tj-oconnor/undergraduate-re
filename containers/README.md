# Containers

We observed throughout the course that standardizing our lab and competition environments on Docker virtualization platforms offered substantial benefits to both instruc- tors and students. During our course, we used the following containers.

## Docker Images

| Container         | Description | 
|-------------|-------------|
| [student-workspace](https://github.com/tj-oconnor/Docker-Images/tree/main/labvm)  | Links to the Dockerfile we distribute to students to use for our [cyber operations concentration](https://research.fit.edu/cyber) courses             |
| [amd64_challenge](amd64_challenge/)            | Links to the Dockefile to host amd64 binaries             |
| [arm_challenge](arm_challenge/)				 | Links to the Dockefile to host armhf binaries   		     |
| [bomb_lab](bomb_lab/)							 | Links to the Dockerfile to host gdb in a webapp for the bomb-lab				|
| [assembly_challenge](assembly_challenge/)  | Links to the Dockerfile to run assembly challenges (not covered in paper)     |

## Deploying containers

We recommend using [ctfd.io](https://ctfd.io) for hosting challenge containers. For the amd64, arm_challenges, and bomb_lab, simply copy over the binary to the ``bin`` and flag to the ``flag`` directory.

For the student workspace, we suggest launching the container with the following settings to enable debugging, tracing, and manipulating binaries. We also map the ``root/workspace`` directory to a local path to maintain a persistent workspace.

```
docker run -v /path/to/local/dir:/root/workspace --cap-add=SYS_PTRACE --cap-add=SYS_ADMIN \
  --cap-add=audit_control --security-opt seccomp=unconfined --privileged -ti labvm 
```
