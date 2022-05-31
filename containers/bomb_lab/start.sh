#!/bin/bash

while [ true ]; do
	su -l user -c "ttyd gdb /home/user/chal 2> /dev/null"
done;
