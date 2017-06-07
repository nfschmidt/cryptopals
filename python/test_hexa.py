import pytest
import hexa

@pytest.mark.parametrize('inbytes,expected', [
    (b'H', b'48'),
    (b'?', b'3F'),
    (b' ', b'20'),
])
def test__encode__1_byte(inbytes, expected):
    result = b''.join(bytes([x]) for x in hexa.encode(inbytes))
    assert expected == result 

@pytest.mark.parametrize('inbytes,expected', [
    (b'Hola', b'486F6C61'),
    (b'?jd!)9', b'3F6A64212939'),
    (b' <Z*+}16L', b'203C5A2A2B7D31364C'),
])
def test__encode__1_byte(inbytes, expected):
    result = b''.join(bytes([x]) for x in hexa.encode(inbytes))
    assert expected == result 

@pytest.mark.parametrize('inbytes,expected', [
    (b'48', b'H'),
    (b'3F', b'?'),
    (b'20', b' '),
])
def test__decode__1_byte(inbytes, expected):
    result = b''.join(bytes([x]) for x in hexa.decode(inbytes))
    assert expected == result 

@pytest.mark.parametrize('inbytes,expected', [
    (b'486F6C61', b'Hola'),
    (b'3F6A64212939', b'?jd!)9'),
    (b'203C5A2A2B7D31364C', b' <Z*+}16L'),
])
def test__encode__1_byte(inbytes, expected):
    result = b''.join(bytes([x]) for x in hexa.decode(inbytes))
    assert expected == result 
