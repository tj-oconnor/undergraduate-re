#!/bin/bash

while [ true ]; do
	su -l user -c "socat -dd TCP4-LISTEN:31337,fork,reuseaddr EXEC:'python3 /home/user/pyshell.py',pty,echo=0,raw,iexten=0"
done;
