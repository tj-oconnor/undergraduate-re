import random
import string
from pyfiglet import Figlet
import randomname


def rand_reg(excluded_regs=[]):
    regs = ['rax', 'rbx', 'rcx', 'rdx', 'rdi', 'rsi', 'r8',
            'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']
    while True:
        reg = random.choice(regs)
        if (reg not in excluded_regs):
            return reg


def rand_ext_reg():
    return rand_reg(excluded_regs=['rax', 'rbx', 'rcx', 'rdx', 'rdi', 'rsi'])


def rand_gp_reg():
    return rand_reg(excluded_regs=['r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15'])

def rand_reg_clobber_free(more_excluded_regs=[]):
    while True:
        reg=rand_reg(excluded_regs=['rax', 'rbx', 'rcx', 'rdx', 'rdi', 'rsi','r8', 'r9', 'r10', 'r11'])
        if (reg not in more_excluded_regs):
           return reg

def rand_op(reg='rax', excluded_regs=[]):
    random_ops = ['inc', 'dec', ]
    random_nops = ['nop', 'xchg rbx, rbx', 'sub rbp, 0x0']
    coin_flip = random.randint(0, 1)
    if (coin_flip == 0):
        return "%s %s; " % (random.choice(random_ops), rand_reg(excluded_regs=excluded_regs))
    else:
        return random.choice(random_nops)


def pop_gadget(reg='rax', pad_len=0):
    excluded_regs = [reg, ]
    chain = "asm(\"pop %%%s; " % reg
    for i in range(pad_len):
        pad_reg = rand_reg(excluded_regs)
        excluded_regs.append(pad_reg)
        chain += "pop %%%s; " % pad_reg
    chain += "ret;\");"
    return chain


def write_gadget(reg1='rdi', reg2='rsi', pad_len=0):
    excluded_regs = [reg1, reg2]
    chain = "asm(\"mov %%%s,(%%%s);  " % (reg1, reg2)
    for i in range(pad_len):
        pad_reg = rand_reg(excluded_regs)
        excluded_regs.append(pad_reg)
        chain += "pop %%%s; " % pad_reg
    chain += "ret;\");"
    return chain


def xfer_gadget(reg1='rdi', reg2='rsi', pad_len=0):
    excluded_regs = [reg1, reg2]
    coin_flip = random.randint(0, 1)
    if (coin_flip == 0):
        chain = chain = "asm(\"mov %%%s,%%%s;  " % (reg1, reg2)
        for i in range(pad_len):
            pad_reg = rand_reg(excluded_regs)
            excluded_regs.append(pad_reg)
            chain += "pop %%%s; " % pad_reg
        chain += "ret;\");"
        return chain
    else:
        chain = chain = "asm(\"push %%%s; pop %%%s;  " % (reg1, reg2)
        for i in range(pad_len):
            pad_reg = rand_reg(excluded_regs)
            excluded_regs.append(pad_reg)
            chain += "pop %%%s; " % pad_reg
        chain += "ret;\");"
        return chain


def syscall_chain():
    chain = "asm(\"syscall; ret;\");"
    return chain


def rand_int(min_num=0, max_num=0xFFFFFFFF):
    return random.randint(min_num, max_num)


def rand_dword(min_num=0, max_num=0xFFFFFFFF):
    return hex(rand_int(min_num, max_num))


def rand_qword(min_num=0, max_num=0xFFFFFFFFFFFFFFFF):
    return hex(rand_int(min_num, max_num))


def rand_char_array(array_len=8):
    array_str = '{'
    for i in range(array_len):
        rand_char = hex(rand_int(65, 122))
        array_str += rand_char+','
    array_str = array_str[:-1]+'}'
    return array_str

fib_array = [0, 1]

def fibonacci(n):
    if n <= len(fib_array):
        return fib_array[n - 1]
    else:
        fib_array.append(fibonacci(n - 1) + fibonacci(n - 2))
        return fib_array[-1]

def rand_min():
    return rand_int(0, 60)


def rand_hr():
    return rand_int(1, 24)


def rand_str(str_len=8):
    letters = string.ascii_lowercase
    letters += string.ascii_uppercase
    return (''.join(random.choice(letters) for i in range(str_len)))


def rand_cmd():
    cmds = ['uname -a', 'ps -ax', 'ls -al', 'uptime', 'whoami']
    return random.choice(cmds)


def rand_word(word_type=random.randint(0, 2)):
    words = {0: random.choice(randomname.VERBS), 1: random.choice(
        randomname.ADJECTIVES), 2: random.choice(randomname.NOUNS)}
    return words[word_type]

def rand_null_word():
    r = rand_word()
    return '\0'.join(r[i:i+1] for i in range(0, len(r), 1))

def header_includes():
    includes = """
    #pragma GCC diagnostic ignored "-Wimplicit-function-declaration"
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <unistd.h>
    #include <sys/syscall.h>
    #include <sys/types.h>
    #include <time.h>
    """
    return includes

def md5_header():
    includes = """
    #include <openssl/md5.h> 
    """
    return includes 

def func_banner(txt=rand_word(),):
    font_list = (
        '6x10', 'acrobatic', 'banner3', 'banner3-D', 'basic', 'big',
        'block', 'broadway', 'char3___', 'chunky', 'clb6x10', 'clr6x10',
        'clr8x8', 'cyberlarge', 'doh', 'doom', 'epic', 'f15_____',
        'gothic', 'graceful', 'larry3d', 'pebbles', 'puffy',
        'rectangles', 'roman', 'rounded', 'serifcap', 'slant', 'standard',
        'starwars', 'univers', 'graffiti'
    )
    custom_fig = Figlet(font=random.choice(font_list))
    lines = (custom_fig.renderText(txt)).split('\n')

    banner = []
    for line in lines:
        banner.append("printf(\"%s\\n \");" % line.replace('\\', '\\\\'))

    return banner


def rand_win_cmd():
    win = ['system("cat flag.txt");', 'system("/bin/sh");']
    return random.choice(win)


def rand_win_func():
    func = """
    void win() {
     %s
    }
    """ % rand_win_cmd()
    return func


def func_display_flag():
    func = """
    void display_flag(char* fname) {
        FILE *fp;
        char buff[255];
        fp = fopen(fname, "r");

        if (fp==NULL) {
            printf("<<< Error: %s is not present", fname);
            exit(0);
        }
        else {
            fscanf(fp, "%s", buff);
            printf("<<< Congratulations: %s\\n", buff );
        }
    }
    """
    return func


def rand_func():
    libc_funcs = ['puts', 'printf', 'rand']
    return random.choice(libc_funcs)


def main_func():
    func = """
    int main() {
       vuln();
       fflush(stdout); 
       return 0;
    }
    """
    return func


def main_chal_func():
    func = """
    int main() {
       challenge();
       fflush(stdout); 
       return 0;
    }
    """
    return func

def func_ignore_me():
    func = """
    __attribute__((constructor)) void ignore_me() {
        setbuf(stdin, NULL);
        setbuf(stdout, NULL);
        setbuf(stderr, NULL);
    }
    """
    return func
