#!/usr/bin/env python
import sys
from itertools import zip_longest

SYMBOLS = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
PADDING_SYMBOL = b'='[0]

def from_bytes(rawbytes):
    for t in triplets_groups(rawbytes):
        yield from from_triplet(t)

def triplets_groups(rawbytes):
    iterables = [iter(rawbytes)] * 3
    yield from zip_longest(*iterables, fillvalue=None)

def from_triplet(triplet):
    assert len(triplet) == 3

    yield SYMBOLS[triplet[0] >> 2]

    if triplet[1] != None:
        yield SYMBOLS[((triplet[0] & 0x03) << 4) | triplet[1] >> 4]

        if triplet[2] != None:
            yield SYMBOLS[((triplet[1] & 0x0F) << 2) | triplet[2] >> 6]
            yield SYMBOLS[(triplet[2] & 0x3F)]
        else:
            yield SYMBOLS[(triplet[1] & 0x0F) << 2]
            yield PADDING_SYMBOL
    else:
        yield SYMBOLS[(triplet[0] & 0x03) << 4]
        yield PADDING_SYMBOL
        yield PADDING_SYMBOL


if __name__ == '__main__':
    def stdin_bytes():
        for i in sys.stdin.buffer:
            yield from i

    for b in from_bytes(stdin_bytes()):
        print(chr(b), end='')
