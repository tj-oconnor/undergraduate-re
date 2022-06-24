#!/bin/bash

while [ true ]; do
     socat TCP-LISTEN:31337,reuseaddr,fork EXEC:"python3 /home/user/pyshell.py"
done;
