import pytest
import vigenere
import xor

mock_length_scorer = lambda rb, length: length
mock_random_scorer = lambda rb, length: [8, 6, 9, 5, 7].index(length)

@pytest.mark.parametrize('rawbytes, start, limit, scorer, expected', [
    (b'this is a test', 1, 6, mock_length_scorer, [5, 4, 3, 2, 1]),
    (b'this is a test', 8, 12, mock_length_scorer, [11, 10, 9, 8]),
    (b'this is a test', 5, 10, mock_random_scorer, [7, 5, 9, 6, 8]),
])
def test__keysizes__returns_keysizes_in_descending_score_order(rawbytes, start, limit, scorer, expected):
    assert expected == vigenere.keysizes(rawbytes, start, limit, scorer)

def mock_xor_scorer(original):
    return lambda rb: 1 if rb in [original[0::4], original[1::4], original[2::4], original[3::4]] else 0

def test__find_key_with_keysize():
    original = b'dk)2hF{"}9!d'
    key = b'1234'
    encrypted = bytes(xor.repeated_xor(key, original))
    keysize = 4

    assert key == vigenere.find_key_with_size(encrypted, keysize, mock_xor_scorer(original))

def test__find_key():
    original = b'dk)2hF{"}9!d'
    key = b'1234'
    encrypted = bytes(xor.repeated_xor(key, original))
    keysize = 4

    mock_keysize_scorer = lambda _, s: 1/s if s <= 4 else 0
    mock_result_scorer = lambda result: 1 if result == original else 0 
    keysize_start = 1
    keysize_limit = 10
    keys_to_try = 5

    assert (key, original) == vigenere.decrypt(
            encrypted,
            keysize_start, keysize_limit, keys_to_try,
            mock_keysize_scorer,
            mock_xor_scorer(original),
            mock_result_scorer)

