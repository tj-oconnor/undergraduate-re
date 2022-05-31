# Automatic Exploit Generation Competition Files

To test your working exploit generation script with the [original binaries](testing/bins/bins.tar.gz), you can copy over your ``aeg.py`` script to the ``solution`` directory and build the container. Then execute ```docker run -it test-aeg python3 /execute_test.py``` to test against the original binaries. Note, the included example below is the [solarpanth3r](https://github.com/tpetersen2018/AutoExploitFinal) script created by Tiffanie Petersen, Carl Mann, and Josh Breinenger. 

If you wish to test with additional binaries, you can create more binaries using the [build framerwork](../build/) that contains pre-existing [templates for vulnerable binaries](../build/templates/competition) for the vulnerabilities described in our paper.

```
$ cp my_solution.py solution/aeg.py

$ docker build -t test-aeg .
<..snipped..>

$ docker run -it test-aeg python3 /execute_test.py

========================================================================================
python3 aeg.py BIN=bins/vuln-88
========================================================================================

CREATING SOLVER FOR: bins/vuln-88
ANALYZING SYMBOLS...
Found a hardcoded gadget: useful_gadget0
Found a call to printf: printf
ANALYZING INPUT/OUTPUT...
[!] Error parsing corefile stack: Found bad environment at 0x7ffe39ffefd7
WARNING | 2022-05-27 10:32:06,163 | pwnlib.elf.corefile | Error parsing corefile stack: Found bad environment at 0x7ffe39ffefd7
End of stack data is b'\x00\x00\x00\x00\x00\x00\x00\x00'
Number of inputs: 1
Input Attack Vectors: {1: ['overflow:40']}
DETERMING EXPLOIT...
ret2system exploit identified
$ whoami
root
$ 
======================================================================================
vuln-88 terminated
======================================================================================

========================================================================================
python3 aeg.py BIN=bins/vuln-29
========================================================================================

CREATING SOLVER FOR: bins/vuln-29
ANALYZING SYMBOLS...
Found a call to printf: printf
ANALYZING INPUT/OUTPUT...
Leak Found! Input:1: Output:<<< Wrong guess: 0x402026

[ERROR] Could not find core file for pid 32
ERROR   | 2022-05-27 10:32:33,670 | pwnlib.tubes.process.process.139976848493200 | Could not find core file for pid 32
Number of inputs: 1
Input Attack Vectors: {1: ['leak']}
DETERMING EXPLOIT...
leak flag off of stack exploit identified
THE FLAG IS: flag{aaaabaaacaaadaaaeaaafaaagaaahaaa}

```