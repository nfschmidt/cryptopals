import xor
import byte

def keysizes(rawbytes, start_length, limit_length, keysize_scorer):
    scores = {length: keysize_scorer(rawbytes, length)
                for length in range(start_length, limit_length)}

    return sorted(scores.keys(), key=scores.get, reverse=True)

def find_key_with_size(rawbytes, keysize, xor_scorer):
    key = b''
    for i in range(keysize):
        block_key, decrypted = xor.decrypt(rawbytes[i::keysize], xor_scorer)
        key += block_key

    return key

def decrypt(rawbytes, keysize_start, keysize_limit, keys_to_try, keysize_scorer, xor_scorer, result_scorer):
    key_sizes = keysizes(rawbytes, keysize_start, keysize_limit, keysize_scorer)

    best = (None, None, None)
    for ks in key_sizes[:keys_to_try]:
        key = find_key_with_size(rawbytes, ks, xor_scorer)
        decrypted = bytes(xor.repeated_xor(key, rawbytes))
        score = result_scorer(decrypted)

        if best[0] == None or score > best[0]:
            best = (score, key, decrypted)

    return (best[1], best[2])

def hamming_distance_scorer(rawbytes, size):
    blocks_count = len(rawbytes) // size
    distances_sum = 0
    for i in range(0, blocks_count, 2):
        distances_sum += byte.hamming_distance(
            rawbytes[size*i:size*(i+1)],
            rawbytes[size*(i+1):size*(i+2)])

    average = distances_sum / (blocks_count / 2) 
    normalized = average / size
    return 1/normalized

def text_characters_scorer(rawbytes):
    valid_bytes = (
        b"abcdefghijklmnopqrstuvwxyz"
        b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b"0123456789.,\n: '?"
    )
    return sum(1 if b in valid_bytes else -100 for b in rawbytes)


if __name__ == '__main__':
    import sys

    def input_bytes():
        for b in sys.stdin.buffer:
            yield from b

    rawbytes = bytes(input_bytes())
    key, decrypted = decrypt(
        rawbytes,
        keysize_start=2,
        keysize_limit=41,
        keys_to_try=10,
        keysize_scorer=hamming_distance_scorer,
        xor_scorer=text_characters_scorer,
        result_scorer=text_characters_scorer
    )

    print(f"Key: {key.decode('utf-8')} {decrypted.decode('utf-8')}")

