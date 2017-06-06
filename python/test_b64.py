import pytest
import b64

@pytest.mark.parametrize("bytes_input,expected", [
    (b'123', b'MTIz'),
    (b'7Zg', b'N1pn'),
    (b'AzU', b'QXpV'),
])
def test__from_bytes__with_3_bytes(bytes_input, expected):
    out = b64.from_bytes(bytes_input)
    result = b''.join(bytes([b]) for b in out)

    assert  expected == result

@pytest.mark.parametrize("bytes_input,expected", [
    (b'pSj3Ka', b'cFNqM0th'),
    (b'ADr86 ', b'QURyODYg'),
    (b'p^.k!s', b'cF4uayFz'),
])
def test__from_bytes__with_bytes_multiple_of_3(bytes_input, expected):
    out = b64.from_bytes(bytes_input)
    result = b''.join(bytes([b]) for b in out)

    assert  expected == result

@pytest.mark.parametrize("bytes_input,expected", [
    (b'pSj3K', b'cFNqM0s='),
    (b'ADr8 ', b'QURyOCA='),
    (b'p^.k!', b'cF4uayE='),
])
def test__from_bytes__1_padding(bytes_input, expected):
    out = b64.from_bytes(bytes_input)
    result = b''.join(bytes([b]) for b in out)

    assert  expected == result

@pytest.mark.parametrize("bytes_input,expected", [
    (b'pSjK', b'cFNqSw=='),
    (b'AD r', b'QUQgcg=='),
    (b'p^.}', b'cF4ufQ=='),
])
def test__from_bytes__2_paddings(bytes_input, expected):
    out = b64.from_bytes(bytes_input)
    result = b''.join(bytes([b]) for b in out)

    assert  expected == result
