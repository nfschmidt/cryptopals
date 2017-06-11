import pytest
import xor

@pytest.mark.parametrize('rawbytes1,rawbytes2,expected', [
    (b'A', b'9', b'\x78'),
    (b'!', b'l', b'\x4d'),
    (b'>', b'{', b'\x45'),
])
def test__fixed_xor__1_byte(rawbytes1, rawbytes2, expected):
    result = b''.join(bytes([x]) for x in xor.fixed_xor(rawbytes1, rawbytes2))
    assert expected == result

@pytest.mark.parametrize('rawbytes1,rawbytes2,expected', [
    (b'AB', b'i9', b'\x28\x7b'),
    (b'!U', b'l>', b'\x4d\x6b'),
    (b'>Fo', b'{*R', b'\x45\x6c\x3d'),
])
def test__fixed_xor__multiple_bytes(rawbytes1, rawbytes2, expected):
    result = b''.join(bytes([x]) for x in xor.fixed_xor(rawbytes1, rawbytes2))
    assert expected == result

@pytest.mark.parametrize('key, rawbytes, expected', [
    (b'a', b'test', b'\x15\x04\x12\x15'),
    (b'*', b'a8!=aS', b'\x4b\x12\x0b\x17\x4b\x79'),
])
def test__repeated_xor__single_byte_key(key, rawbytes, expected):
    result = b''.join(bytes([x]) for x in xor.repeated_xor(key, rawbytes))
    assert expected == result

@pytest.mark.parametrize('key, rawbytes, expected', [
    (b'abc', b'test', b'\x15\x07\x10\x15'),
    (b'*(gj', b'a8!=aS', b'\x4b\x10\x46\x57\x4b\x7b'),
    (b'097h1lh', b'a8', b'\x51\x01'),
])
def test__repeated_xor__multiple_bytes_key(key, rawbytes, expected):
    result = b''.join(bytes([x]) for x in xor.repeated_xor(key, rawbytes))
    assert expected == result

def test__decrypt_single_byte__returns_best_score_result():
    plain = b'test plain text'
    key = b'X'
    scoring = lambda b: 1 if b == plain else 0
    
    encrypted = bytes(xor.repeated_xor(key, plain))
    expected = (key, plain)
    assert expected == xor.decrypt(encrypted, scoring)


