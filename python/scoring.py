#!/usr/bin/env python
import sys
from functools import partial

_ENGLISH_LOWER_FREQUENCIES = [
    ('a', 8167),
    ('b', 1492),
    ('c', 2782),
    ('d', 4253),
    ('e', 12702),
    ('f', 2228),
    ('g', 2015),
    ('h', 6094),
    ('i', 6966),
    ('j', 153),
    ('k', 772),
    ('l', 4025),
    ('m', 2406),
    ('n', 6749),
    ('o', 7507),
    ('p', 1929),
    ('q', 95),
    ('r', 5987),
    ('s', 6327),
    ('t', 9056),
    ('u', 2758),
    ('v', 978),
    ('w', 2360),
    ('x', 150),
    ('y', 1974),
    ('z', 74),
]

ENGLISH_FREQUENCIES = {
    **{bytes(c, 'utf-8')[0]: v for c, v in _ENGLISH_LOWER_FREQUENCIES},
    **{bytes(c.upper(), 'utf-8')[0]: v for c, v in _ENGLISH_LOWER_FREQUENCIES}
}

SPACE_FREQUENCIES = {b' '[0]: 1}

def byte_frequency(rawbytes, frequency_table):
    return sum(frequency_table.get(r, 0) for r in rawbytes)

def scorer(frequency_table):
    return partial(byte_frequency, frequency_table=frequency_table)


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'bytefreq':
        if sys.argv[2] == 'en':
            action = scorer(ENGLISH_FREQUENCIES)
        if sys.argv[2] == 'space':
            action = scorer(SPACE_FREQUENCIES)
    else:
        print("ERROR", file=sys.stderr)
        exit(1)

    def stdin_bytes():
        for bs in sys.stdin.buffer:
            yield from bs

    print(action(stdin_bytes()))
