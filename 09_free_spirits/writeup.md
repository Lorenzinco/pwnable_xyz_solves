# 09 Free spirits

The challege wants me to learn some stuff about heap exploitation, which i indeed did.
Basically there's this struct that has 2 fields, the first one is just garbage, thrown there to make the struct 16 bytes long, the second one is a pointer to the heap, which is allocated with malloc.

The intresting part is that there's a function which can be accessed by typing 3, which takes the pointed in the heap and throws it in the struct.

with the struct being defined in ida as follows:

```c
struct my_struct{
    double garbage;
    void *ptr;
}
```

the function that takes the pointer and throws it in the struct is defined as follows:

```c
if ( choice == 3 )
{
   mystruct = (my_struct *)mystruct->ptr;
}
```

So by filling the heap, first with some 8 bytes garbage and then with some other 8 bytes and performing the function we can overwrite the pointer in the struct and have and arbitrary write primitive.

Using this method we can overwrite the return address with the nop slide and win function by having the stack leaked from inserting "2".

The next step (the intresting one) is to make the free not fail. In order to do so we need to give the free function which is called at the end of the program before returning a valid pointer, so that it doesn't fail.

We can craft a fake fastbin heap chunk as follows:

```py
#struct fast_chunk {
#  size_t prev_size;
#  size_t size;
#  struct fast_chunk *fd;
#  struct fast_chunk *bk;
#  char buf[0x20];                   // chunk falls in fastbin size range
#};
fake_chunk = b'A'*8
fake_chunk += p64(retAddrStackAddr+32)
fake_chunk += p64(0x40) #prev_size 8
fake_chunk += p64(0x40) #size 16
fake_chunk += p64(retAddrStackAddr+48) #fd
fake_chunk += p64(retAddrStackAddr+48) #bk
fake_chunk += b'D' * 0x20
```

This above is a perfectly valid fastbin chunk, but it has a problem: it's description is too long, the read function will discard half of my input and pipe it to the next scanf of the program which i surely don't want.

So by fuzzing and discarding 8 bytes at a time from the fake chunk i found out that after the size field none of the fields really matter anymore, as long as the pointer points to the data section of the bin, the only valid fields are the size one, which has to be 0x40 and the previous size one, which since it's a fastbin chunk also has to be 0x40.

