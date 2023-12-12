import random
import string
from pyfiglet import Figlet, figlet_format
import randomname
import json


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
        reg = rand_reg(excluded_regs=[
                       'rax', 'rbx', 'rcx', 'rdx', 'rdi', 'rsi', 'r8', 'r9', 'r10', 'r11'])
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


def rand_list(item_size=4):
    rand_items = """
    char * items[] = {
    """
    for _ in range(0, item_size):
        rand_items += """\"%s\\0\",
        """ % (rand_word(1)+"_"+rand_word(2))
    rand_items += """NULL
    };
    """
    return rand_items


def rand_chaf(item_size=4):
    return rand_list(item_size).replace('items[]', 'chaf[]')


def rand_null_word():
    r = rand_word()
    return '\0'.join(r[i:i+1] for i in range(0, len(r), 1))


def header_includes():
    includes = """
    #pragma GCC diagnostic ignored "-Wimplicit-function-declaration"
    #define _GNU_SOURCE
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <unistd.h>
    #include <dlfcn.h>
    #include <sys/syscall.h>
    #include <sys/types.h>
    #include <time.h>
    #include <stdint.h>

    extern void __libc_csu_init(void);
    """
    return includes


def md5_header():
    includes = """
    #include <openssl/md5.h> 
    """
    return includes


def func_banner(txt=rand_word(1)+"_"+rand_word(2),):
    custom_fig = figlet_format(txt)
    escaped_banner = json.dumps(custom_fig)
    banner = f'printf({escaped_banner});\n'
    return banner


def rand_win_cmd():
    win = ['system("cat flag.txt");', 'system("/bin/sh");']
    return random.choice(win)


def rand_win_char():
    win = ['char cmd[]="cat flag.txt";', 'char cmd[]="/bin/sh";']
    return random.choice(win)


def rand_win_func():
    func = """
    void win() {
     %s
    }
    """ % rand_win_cmd()
    return func

def check_target(buffersize,sizecheck):
    func = """  
    int count = 0;
    if (memmem(buf+%i+8, %i, bytes, 8) !=NULL ) {
      exit(0);
    }
    """ %(buffersize,sizecheck)
    return func

def define_target():
    func = """
    char bytes[8];

    uint64_t addr = 0;
    addr |= (uint64_t)(target & 0xFF) << 56;
    addr |= (uint64_t)(target & 0xFF00) << 40;
    addr |= (uint64_t)(target & 0xFF0000) << 24;
    addr |= (uint64_t)(target & 0xFF000000) << 8;

    bytes[0] = (addr >> 56) & 0xFF;
    bytes[1] = (addr >> 48) & 0xFF;
    bytes[2] = (addr >> 40) & 0xFF;
    bytes[3] = (addr >> 32) & 0xFF;
    bytes[4] = (addr >> 24) & 0xFF;
    bytes[5] = (addr >> 16) & 0xFF;
    bytes[6] = (addr >> 8) & 0xFF;
    bytes[7] = addr & 0xFF;
    """
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
    txt = rand_word(1)+"_"+rand_word(2)
    func = """
    int main() {
       %s

       vuln();
       
       printf(\"\\n<<< Goodbye\\n\");
       return 0;
    }
    """ % func_banner(txt)
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
