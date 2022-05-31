import binaryninja as bn
import json
import os


def get_json():
    pwd = os.path.dirname(__file__)
    json_path = os.path.join(pwd, 'syscall.json')
    with open(json_path) as file:
        data = json.load(file)
    return data

# Get port and IP from a network-byte long


def get_address(num):
    response = ''
    tmp = (num & 0xFFFF0000) >> 16
    port = ((tmp << 8) | (tmp >> 8)) & 0xFFFF
    tmp = num >> 32
    ip = f"{tmp&0xFF}.{(tmp>>8)&0xFF}.{(tmp>>16)&0xFF}.{(tmp>>24)&0xFF}"
    return f":IP={ip} & Port={port}"


def run(bv):
    # Get our JSON file & list of registers
    syscalls = get_json()
    registers = bv.platform.system_call_convention.int_arg_regs
    # Nested loop to go through each instruction looking for a syscall
    for function in bv.functions:
        for block in function.low_level_il:
            for i in block:
                # and i.get_reg_value('rax') == 0x29):
                if (i.operation == bn.LowLevelILOperation.LLIL_SYSCALL):
                    # Get syscall number from rax register
                    rax = i.get_reg_value('rax').value
                    if str(rax) in syscalls:
                        call = syscalls[str(rax)]
                        comment = f"{call['name']} Syscall -"
                        # Iterate over each argument
                        for reg, arg in enumerate(call['args']):
                            reg_val = i.get_reg_value(registers[reg+1]).value
                            comment += f"  {arg['name']}"
                            # If the argument selects from a specific option, get the value of that option
                            if arg['type'] == 'option':
                                comment += f":{arg['options'][str(reg_val)]}"
                            # If the argument can be multitude of values, just get what the value is
                            if arg['type'] == 'value':
                                if reg_val == None:     # Value determinable only during runtime
                                    comment += "=<RuntimeValue>"
                                else:
                                    comment += f"={reg_val}"
                            if arg['type'] == 'pointer':
                                # Get offset it is from stack
                                offset = int(
                                    str(i.get_reg_value(registers[reg+1])).split()[-1].strip('>'), 16)
                                num = i.get_stack_contents(offset, 8).value
                                # If bind() or connect(), grab the IP and Port from the sockaddr struct; else just get value
                                if rax == 49 or rax == 42:
                                    comment += get_address(num)
                                else:
                                    comment += f"={i.get_stack_contents(offset, 8)}"
                            if arg['type'] == 'reference':
                                comment += f"<PeerProvidedValue>"
                        # Add comment
                        function.set_comment_at(i.address, comment)
