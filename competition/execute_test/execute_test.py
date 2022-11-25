import os
import colorama
from colorama import Fore, Style
from pwn import *

SOLUTION = '/solution/aeg.py'

if args.BIN_DIR:
   BIN_DIR=args.BIN_DIR
else:
   BIN_DIR  = '/bins/'

for bin in os.listdir(BIN_DIR):
   filename = "%s%s" %(BIN_DIR,bin)
   if os.access(filename, os.X_OK):
        cmd = "python3 %s BIN=%s" %(SOLUTION,filename)
        print(Fore.RED+"\n========================================================================================")
        print(Fore.GREEN+cmd)
        print(Fore.RED+"========================================================================================")
        print(Style.RESET_ALL)
        os.system(cmd)
        print(Fore.GREEN+"======================================================================================")
        print(Fore.RED+bin+" terminated")
        print(Fore.GREEN+"======================================================================================")
