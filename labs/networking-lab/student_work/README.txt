# AUTHOR -  Carl Mann
# CLASS  -  CSE4830

This plugin comments above network system calls in Binary Ninja. The plugin currently
assumes the architecture is Linux x86-64 for the binary.

It relies on a syscall.json file to determine the number of arguments, names of the parameters, and how to interpret
the values passed in. This syscall.json file can be expanded to have more system calls, or even refactored to account
for different architectures.