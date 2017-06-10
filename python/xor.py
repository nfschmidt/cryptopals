#!/usr/bin/env python
import sys

def fixed_xor(rawbytes1, rawbytes2):
    return (int(b1)^int(b2) for b1, b2 in zip(rawbytes1, rawbytes2))



if __name__ == '__main__':
    if len(sys.argv) == 4 and sys.argv[1] == 'fixor':
        action = fixed_xor
    else:
        print("ERROR", file=sys.stdout)
        exit(1)

    def bytes_from_file(f):
        with open(f, 'rb') as content:
            for c in content:
                yield from c

    rawbytes1 = bytes_from_file(sys.argv[2])
    rawbytes2 = bytes_from_file(sys.argv[3])
    for b in action(rawbytes1, rawbytes2):
        sys.stdout.buffer.write(bytes([b]))
