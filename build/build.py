
import jinja2
import os
import sys
import tempfile
from helper_funcs import *

def compile(source_code, bin_name, flags='-no-pie -fno-stack-protector -fno-builtin -Wno-all -Wno-extra'):
    source_file = tempfile.NamedTemporaryFile(
        mode='w', buffering=- 1, suffix='.c', prefix='src-', dir='./src', delete=False)
    source_file.write(source_code)
    source_file.close()
    cmd = 'gcc -o bin/%s %s %s ' % (
        bin_name, source_file.name, flags)
    os.system(cmd)


def arm_compile(source_code, bin_name, flags='-no-pie -fno-stack-protector'):
    source_file = tempfile.NamedTemporaryFile(
        mode='w', buffering=- 1, suffix='.c', prefix='src-', dir='./src', delete=False)
    source_file.write(source_code)
    source_file.close()
    cmd = 'arm-linux-gnueabihf-gcc -o bin/%s %s %s ' % (
        bin_name, source_file.name, flags)
    os.system(cmd)

def gen_ret2win(bin_name):
    template = jinja2.Template(
        open('templates/competition/ret2win.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), win_func=rand_win_func(), buffersize=rand_int(
        0x32, 0xff), greeting=rand_word(), closing=rand_word(), ignore_me=func_ignore_me(), main=main_func())
    compile(source_code, bin_name)


def gen_ret2execve(bin_name):
    template = jinja2.Template(
        open('templates/competition/ret2execve.c.jinja', 'r').read())
    pop_rdi = pop_gadget(reg='rdi', pad_len=rand_int(0, 3))
    pop_rsi = pop_gadget(reg='rsi', pad_len=rand_int(0, 3))
    pop_rdx = pop_gadget(reg='rdx', pad_len=rand_int(0, 3))
    pop_rcx = pop_gadget(reg='rcx', pad_len=rand_int(0, 3))
    source_code = template.render(header=header_includes(), pop_rdi=pop_rdi, pop_rsi=pop_rsi, pop_rdx=pop_rdx, pop_rcx=pop_rcx, buffersize=rand_int(
        0x32, 0xff), greeting=rand_word(), prompt=rand_word(), closing=rand_word(), ignore_me=func_ignore_me(), main=main_func())
    compile(source_code, bin_name)


def gen_ret2syscall(bin_name):
    template = jinja2.Template(
        open('templates/competition/ret2syscall.c.jinja', 'r').read())
    pop_rdi = pop_gadget(reg='rdi', pad_len=rand_int(0, 3))
    pop_rsi = pop_gadget(reg='rsi', pad_len=rand_int(0, 3))
    pop_rdx = pop_gadget(reg='rdx', pad_len=rand_int(0, 3))
    pop_rax = pop_gadget(reg='rax', pad_len=rand_int(0, 3))
    source_code = template.render(header=header_includes(), pop_rdi=pop_rdi, pop_rsi=pop_rsi, pop_rdx=pop_rdx, pop_rax=pop_rax, buffersize=rand_int(
        0x32, 0xff), rand_word=rand_word(), prompt=rand_word(), closing=rand_word(), syscall_gadget=syscall_chain(), ignore_me=func_ignore_me(), main=main_func())
    compile(source_code, bin_name)


def gen_ret2system(bin_name):
    template = jinja2.Template(
        open('templates/competition/ret2system.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), buffersize=rand_int(0x32, 0xff), rand_cmd=rand_cmd(
    ), closing=rand_word(), prompt=rand_word(), rand_word1=rand_word(), rand_word2=rand_word(), ignore_me=func_ignore_me(), main=main_func())
    compile(source_code, bin_name)


def gen_ret2one(bin_name):
    template = jinja2.Template(
        open('templates/competition/ret2one.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), buffersize=rand_int(
        0x32, 0xff), rand_func=rand_func(), prompt=rand_word(), closing=rand_word(), ignore_me=func_ignore_me(), main=main_func())
    compile(source_code, bin_name)


def gen_rop_parameters(bin_name):
    template = jinja2.Template(
        open('templates/competition/ropparams.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), rand_val1=rand_int(0x32, 0xff), rand_val2=rand_int(0x32, 0xff), win_cmd=rand_win_cmd(), buffersize=rand_int(
        0x32, 0xff), rand_func=rand_func(), rand_word=rand_word(), greeting=rand_word(), closing=rand_word(), ignore_me=func_ignore_me(), main=main_func())
    compile(source_code, bin_name)


def gen_write_gadgets(bin_name):
    reg1 = rand_gp_reg()
    reg2 = rand_ext_reg()
    pop_reg1 = pop_gadget(reg=reg1, pad_len=rand_int(0, 3))
    pop_reg2 = pop_gadget(reg=reg2, pad_len=rand_int(0, 3))
    pop_rdi = pop_gadget(reg='rdi', pad_len=rand_int(0, 3))
    mov_reg1_reg2 = write_gadget(reg1=reg1, reg2=reg2, pad_len=rand_int(0, 3))
    template = jinja2.Template(
        open('templates/competition/ropwrite.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), buffersize=rand_int(0x32, 0xff), greeting=rand_word(), prompt=rand_word(), closing=rand_word(
    ), ignore_me=func_ignore_me(), pop_reg1=pop_reg1, pop_reg2=pop_reg2, pop_rdi=pop_rdi, mov_reg1_reg2=mov_reg1_reg2, rand_cmd=rand_cmd(), main=main_func())
    compile(source_code, bin_name)


def gen_printf_read_var(bin_name):
    template = jinja2.Template(
        open('templates/competition/printfrvar.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), buffersize=rand_int(0x16, 0xff), greeting=rand_word(
    ), prompt1=rand_word(), prompt2=rand_word(), closing=rand_word(), ignore_me=func_ignore_me(), main=main_func())
    compile(source_code, bin_name)


def gen_printf_read_libc(bin_name):
    template = jinja2.Template(
        open('templates/competition/printfrlibc.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), buffersize=rand_int(64, 0xff), greeting=rand_word(
    ), prompt=rand_word(), ignore_me=func_ignore_me(), main=main_func())
    compile(source_code, bin_name)


def gen_printf_write_var(bin_name):
    template = jinja2.Template(
        open('templates/competition/printfwlocal.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), buffersize=rand_int(0x16, 0xff), greeting=rand_word(
    ), resp=rand_word(), rand_val=rand_int(0x32, 0xff), ignore_me=func_ignore_me(), main=main_func(), win_func=rand_win_func())
    compile(source_code, bin_name)


def gen_printf_got_overwrite(bin_name):
    template = jinja2.Template(
        open('templates/competition/printfwgot.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), buffersize=rand_int(0xff, 0xffff), greeting=rand_word(
    ), closing=rand_word(), ignore_me=func_ignore_me(), main=main_func(), win_func=rand_win_func())
    compile(source_code, bin_name)


def build_bomb_lab():
    print("[+] Randomly generating and compiling bomblab.")
    template = jinja2.Template(
        open('templates/bomb-lab/bomblab.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), ignore_me=func_ignore_me(), phase1_word=rand_word(), phase2_int=rand_int(
        0x32, 0xffff), phase3_str=rand_str(), phase4_int=rand_int(1, 10), phase5_letters=rand_char_array(array_len=19), display_flag_fname=func_display_flag())
    compile(source_code, "bomblab")


def gen_math_100(bin_name):
    template = jinja2.Template(
        open('templates/math-chals/math100.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), ignore_me=func_ignore_me(
    ), display_flag=func_display_flag(), rand_int=rand_int(0x8, 0xf), main=main_chal_func())
    compile(source_code, bin_name, flags='-no-pie -s')


def gen_math_200(bin_name):
    template = jinja2.Template(
        open('templates/math-chals/math200.c.jinja', 'r').read())
    rv1 = rand_int(0x2, 0xffff)
    rv2 = rand_int(0x2, 0xffff)
    rv3 = rand_int(0x2, 0xffff)
    rv4 = rand_int(0x2, 0xffff)
    rv5 = rand_int(0x2, 0xffff)
    rv6 = rand_int(0x2, 0xffff)
    rv7 = rand_int(0x2, 0xffff)
    rv8 = rand_int(0x2, 0xffff)
    rv9 = rand_int(0x2, 0xffff)
    rv10 = rand_int(0x2, 0xffff)
    source_code = template.render(header=header_includes(), ignore_me=func_ignore_me(), display_flag=func_display_flag(
    ), rv1=rv1, rv2=rv2, rv3=rv3, rv4=rv4, rv5=rv5, rv6=rv6, rv7=rv7, rv8=rv8, rv9=rv9, rv10=rv10, main=main_chal_func())
    compile(source_code, bin_name, flags='-no-pie -s')


def gen_math_300(bin_name):
    template = jinja2.Template(
        open('templates/math-chals/math300.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), ignore_me=func_ignore_me(
    ), display_flag=func_display_flag(), rv_fib=fibonacci(rand_int(10, 54)), main=main_chal_func())
    compile(source_code, bin_name, flags='-no-pie -s')


def gen_math_400(bin_name):
    template = jinja2.Template(
        open('templates/math-chals/math400.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(
    ), ignore_me=func_ignore_me(), display_flag=func_display_flag(), main=main_chal_func())
    compile(source_code, bin_name, flags='-no-pie -s')


def gen_arm_100(bin_name):
    template = jinja2.Template(
        open('templates/arm-chals/arm100.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), ignore_me=func_ignore_me(
    ), display_flag=func_display_flag(), main=main_chal_func(), rand_word=rand_word())
    arm_compile(source_code, bin_name, flags='-no-pie')


def gen_arm_200(bin_name):
    template = jinja2.Template(
        open('templates/arm-chals/arm200.c.jinja', 'r').read())
    r_min = rand_int(0, 30)
    r_max = r_min + 15
    source_code = template.render(header=header_includes(), ignore_me=func_ignore_me(), display_flag=func_display_flag(
    ), main=main_chal_func(), rand_hr=rand_int(9, 16), rand_min_min=r_min, rand_min_max=r_max)
    arm_compile(source_code, bin_name, flags='-no-pie')


def gen_arm_300(bin_name):
    template = jinja2.Template(
        open('templates/arm-chals/arm300.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(
    ), ignore_me=func_ignore_me(), display_flag=func_display_flag(), main=main_chal_func())
    arm_compile(source_code, bin_name, flags='-no-pie')


def gen_arm_400(bin_name):
    template = jinja2.Template(
        open('templates/arm-chals/arm400.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), md5_header=md5_header(
    ), ignore_me=func_ignore_me(), display_flag=func_display_flag(), main=main_chal_func(),rand_int=rand_int(1, 26),rand_word=rand_str(str_len=8))
    arm_compile(source_code, bin_name, flags='-no-pie')


def gen_angry_100(bin_name):
    template = jinja2.Template(
        open('templates/angry-chals/angry100.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), ignore_me=func_ignore_me(
    ), display_flag=func_display_flag(), main=main_chal_func(),buffersize=rand_int(0x8,0xf))
    compile(source_code, bin_name)


def gen_angry_200(bin_name):
    template = jinja2.Template(
        open('templates/angry-chals/angry200.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), ignore_me=func_ignore_me(
    ), display_flag=func_display_flag(), main=main_chal_func(),buffersize=2)
    compile(source_code, bin_name)


def gen_angry_300(bin_name):
    reg1 = rand_reg_clobber_free()
    reg2 = rand_reg_clobber_free(more_excluded_regs=[reg1, ])
    reg3 = rand_reg_clobber_free(more_excluded_regs=[reg1, reg2, ])

    template = jinja2.Template(
        open('templates/angry-chals/angry300.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), ignore_me=func_ignore_me(), display_flag=func_display_flag(
    ), main=main_chal_func(), reg1=reg1, reg2=reg2, reg3=reg3)
    compile(source_code, bin_name)


def gen_angry_400(bin_name):
    template = jinja2.Template(
        open('templates/angry-chals/angry400.c.jinja', 'r').read())
    source_code = template.render(header=header_includes(), ignore_me=func_ignore_me(
    ), display_flag=func_display_flag(), main=main_chal_func())
    compile(source_code, bin_name)


def build_math_lab():
    print("[+] Randomly generating and compiling math challenges.")
    gen_math_100("math-100")
    gen_math_200("math-200")
    gen_math_300("math-300")
    gen_math_400("math-400")


def build_arm_lab():
    print("[+] Randomly generating and compiling arm challenges.")
    gen_arm_100("arm-100")
    gen_arm_200("arm-200")
    gen_arm_300("arm-300")
    gen_arm_400("arm-400")


def build_angry_lab():
    print("[+] Randomly generating and compiling AngrY challenges.")
    gen_angry_100("angry-100")
    gen_angry_200("angry-200")
    gen_angry_300("angry-300")
    gen_angry_400("angry-400")


def build_competition_bins():

    print("[+] Randomly generating and compiling competition binaries.")
    for bin_cnt in range(0,10):
        bin_name = 'bin-ret2win-%i' % bin_cnt
        gen_ret2win(bin_name)

        bin_name = 'bin-ret2execve-%i' % bin_cnt
        gen_ret2execve(bin_name)
        
        bin_name = 'bin-ret2syscall-%i' % bin_cnt
        gen_ret2syscall(bin_name)
        
        bin_name = 'bin-ret2system-%i' % bin_cnt
        gen_ret2system(bin_name)
        
        bin_name = 'bin-ret2one-%i' % bin_cnt
        gen_ret2one(bin_name)
        
        bin_name = 'bin-write_gadgets-%i' % bin_cnt
        gen_write_gadgets(bin_name)
        
        bin_name = 'bin-printf_read_var-%i' % bin_cnt
        gen_printf_read_var(bin_name)
        
        #bin_name = 'bin-printf_read_libc-%i' % bin_cnt
        #gen_printf_read_libc(bin_name)
        
        bin_name = 'bin-printf_write_var-%i' % bin_cnt
        gen_printf_write_var(bin_name)

        bin_name = 'bin-got_overwrite-%i' % bin_cnt
        gen_printf_got_overwrite(bin_name)

        bin_name = 'bin-rop_parameters-%i' % bin_cnt
        gen_rop_parameters(bin_name)
        

if __name__ == '__main__':
    build_type = sys.argv[1]
    if build_type=='bomb-lab':
        build_bomb_lab()
    elif build_type =='math-lab':
        build_math_lab()
    elif build_type=='arm-lab':
        build_arm_lab()
    elif build_type=='angry-lab':
        build_angry_lab()
    elif build_type=='competition':
        build_competition_bins()
    elif build_type=='all':
        build_competition_bins()
        build_bomb_lab()
        build_math_lab()
        build_arm_lab()
        build_angry_lab()
    else:
        print("Error: please specify [bomb-lab | math-lab | arm-lab | angry-lab | competition | all]")
        exit(-1)
