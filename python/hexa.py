#!/usr/bin/env python
import sys

SYMBOLS = b'0123456789ABCDEF'
VALUES = {s: v for (v, s) in enumerate(SYMBOLS)}

def encode(inbytes):
    for b in inbytes:
        yield SYMBOLS[b >> 4]
        yield SYMBOLS[b & 0x0F]

def decode(inbytes):
    nibble_iter = iter(inbytes)
    for n1, n2 in zip(nibble_iter, nibble_iter):
        yield VALUES[n1] << 4 | VALUES[n2]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        action = encode
    elif len(sys.argv) != 2:
        print("ERROR")
        exit(1)
    elif sys.argv[1] == 'encode':
        action = encode
    elif sys.argv[1] == 'decode':
        action = decode
    else:
        print("ERROR")
        exit(1)

    def stdin_bytes():
        for i in sys.stdin.buffer:
            yield from i

    for b in action(stdin_bytes()):
        sys.stdout.buffer.write(bytes([b]))
