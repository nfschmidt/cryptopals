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
