for i in bv.llil_instructions:
    if (i.operation == LowLevelILOperation.LLIL_SYSCALL and i.get_reg_value('rax') == 0x29):
         _domain=''
         _type=''
         if (i.get_reg_value('rdi')==0x2): 
             _domain='IPv4'
         if (i.get_reg_value('rsi')==0x1):
             _type='TCP'
         bv.set_comment_at(i.address,"bind call: domain{%s}, type{%s}" %(_domain,_type))
