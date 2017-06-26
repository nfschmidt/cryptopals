#!/usr/bin/env python
import sys
import itertools
import scoring
import byte

def fixed_xor(rawbytes1, rawbytes2):
    return (int(b1)^int(b2) for b1, b2 in zip(rawbytes1, rawbytes2))

def repeated_xor(key, rawbytes):
    return fixed_xor(itertools.cycle(key), rawbytes)

def decrypt(encrypted, scorer):
    best = (None, None, None)
    for key in (bytes([b]) for b in range(0, 256)):
        decrypted = bytes(repeated_xor(key, encrypted))
        score = scorer(decrypted) 
        if best[0] == None or score > best[0]:
            best = (score, key, decrypted)

    return (best[1], best[2])


if __name__ == '__main__':
    if len(sys.argv) == 4 and sys.argv[1] == 'fixor':
        action = fixed_xor
    elif len(sys.argv) == 4 and sys.argv[1] == 'rexor':
        action = repeated_xor
    elif len(sys.argv) == 4 and sys.argv[1] == 'decrypt' and sys.argv[2] == 'single':
        if sys.argv[3] == 'en':
            scorer = scoring.scorer(scoring.ENGLISH_FREQUENCIES)
        if sys.argv[3] == 'space':
            scorer = scoring.scorer(scoring.SPACE_FREQUENCIES)

        def stdin_bytes():
            for b in sys.stdin.buffer:
                yield from b

        encrypted = bytes(stdin_bytes())
        print('Key: {}\nMessage: {}'.format(*decrypt(encrypted, scorer)))
        exit(0)
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
