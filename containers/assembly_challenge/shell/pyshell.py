from qiling import *
import time
import sys

FLAG = '/home/user/flag.txt'

def main():
    print("==============================================")
    print(open(__file__).read())
    print("==============================================")

    print("PWNME >>> ")
    shellcode = input().encode()

    if ((not shellcode.isalnum()) or (len(shellcode) > 10)):
       print("[+] Fail.")
       return

    ql = Qiling(code=shellcode, 
            rootfs="/rootfs/x86_linux/",
            ostype="linux",
            archtype="x8664")

    ql.arch.regs.rax=0x0
    ql.run()

    if (ql.arch.regs.rax==0x41424344):
        print(open(FLAG).readline())
        sys.stdout.flush()
        time.sleep(15)
   
if __name__ == "__main__":
    main()

