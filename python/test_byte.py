import pytest
import byte

@pytest.mark.parametrize('b1, b2, expected', [
    (bytes([0b11000000]), bytes([0b10000001]), 2),
    (bytes([0b11000000]), bytes([0b00000001]), 3),
    (bytes([0b11000000]), bytes([0b10001111]), 5),
])
def test__hamming_distance__single_byte(b1, b2, expected):
    assert byte.hamming_distance(b1, b2) == expected

@pytest.mark.parametrize('bytes1, bytes2, expected', [
    (b'\x01\x01\x01', b'\x01\x01\x00', 1),
    (b'\x01\x01\x01', b'\x01\x00\x00', 2),
    (b'\x01\x01\x01', b'\x00\x00\x00', 3),
])
def test__hamming_distance__multiple_bytes(bytes1, bytes2, expected):
    assert byte.hamming_distance(bytes1, bytes2) == expected



