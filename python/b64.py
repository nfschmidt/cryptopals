#!/usr/bin/env python
import sys
from itertools import zip_longest

SYMBOLS = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
PADDING_SYMBOL = b'='[0]
VALUES = {s: i for (i, s) in enumerate(SYMBOLS)}


def encode(rawbytes):
    for triplet in tuples_of(3, rawbytes):
        # Symbol corresponding to the first 6 bits of the first byte
        yield SYMBOLS[triplet[0] >> 2]

        if triplet[1] != None:
            # No double padding
            # Symbol corresponding to the last 2 bits of the first byte
            # and first 4 bits of the second byte
            yield SYMBOLS[((triplet[0] & 0x03) << 4) | triplet[1] >> 4]

            if triplet[2] != None:
                # No double padding
                # Symbols corresponding to last 4 bits of second byte and
                # first 2 of the third byte, and last 6 bits of the third byte
                yield SYMBOLS[((triplet[1] & 0x0F) << 2) | triplet[2] >> 6]
                yield SYMBOLS[(triplet[2] & 0x3F)]
            else:
                # Single padding
                # Symbol corresponding to last 4 bits of second byte, and padding
                yield SYMBOLS[(triplet[1] & 0x0F) << 2]
                yield PADDING_SYMBOL
        else:
            # Double padding
            # Symbol corresponding to last 2 bits of first byte, and 2 paddings
            yield SYMBOLS[(triplet[0] & 0x03) << 4]
            yield PADDING_SYMBOL
            yield PADDING_SYMBOL

def decode(b64in):
    for quad in tuples_of(4, b64in):
        b0, b1, b2, b3 = [VALUES.get(b, None) for b in quad]
        yield (b0 << 2) | (b1 >> 4)

        if b2 != None:
            yield ((b1 << 4) & 0xFF) | (b2 >> 2)

        if b3 != None:
            yield ((b2 << 6) & 0xFF) | b3

def tuples_of(length, iterable):
    iterables = [iter(iterable)] * length
    yield from zip_longest(*iterables, fillvalue=None)

def _error(*args, **kwargs):
    print("Error: invalid argument(s)", file=sys.stderr)
    print("Usage: {} [encode | decode]".format(sys.argv[0]), file=sys.stderr)
    exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        action = encode
    elif len(sys.argv) != 2:
        action = _error
    elif sys.argv[1] == 'encode':
        action = encode
    elif sys.argv[1] == 'decode':
        action = decode
    else:
        action = _error

    def stdin_bytes():
        for i in sys.stdin.buffer:
            yield from i

    for b in action(stdin_bytes()):
        sys.stdout.buffer.write(bytes([b]))
