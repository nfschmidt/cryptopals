
def hamming_distance(bytes1, bytes2):
    distance = 0
    for b1, b2 in zip(bytes1, bytes2):
        xored = b1^b2
        distance += sum(1 for n in range(8) if (xored >> n) & 0x01)

    return distance
