import pytest
import scoring

MOCK_SCORES = {
    b'a'[0]: 10,
    b'b'[0]: 20,
    b'c'[0]: 30,
}


@pytest.mark.parametrize('rawbyte, expected', [
    (b'a', 10),
    (b'b', 20),
    (b'c', 30),
])
def test__byte_frequency__single_byte_score(rawbyte, expected):
    assert expected == scoring.byte_frequency(rawbyte, MOCK_SCORES)

@pytest.mark.parametrize('rawbyte, expected', [
    (b'!', 0),
    (b'_', 0),
])
def test__byte_frequency__unknown_bytes_dont_score(rawbyte, expected):
    assert expected == scoring.byte_frequency(rawbyte, MOCK_SCORES)


def test__byte_frequency__multiple_bytes_score():
    rawbytes = b'abcabb'
    expected = 10 + 20 + 30 + 10 + 20 + 20
    assert expected == scoring.byte_frequency(rawbytes, MOCK_SCORES)

