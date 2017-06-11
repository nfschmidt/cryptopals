import pytest
import b64

def transform_test(transform, in_value, expected):
    out = transform(in_value)
    result = bytes(out)
    assert  expected == result


@pytest.mark.parametrize("bytes_input,expected", [
    (b'123', b'MTIz'),
    (b'7Zg', b'N1pn'),
    (b'AzU', b'QXpV'),
])
def test__encode__with_3_bytes(bytes_input, expected):
    transform_test(b64.encode, bytes_input, expected)

@pytest.mark.parametrize("bytes_input,expected", [
    (b'pSj3Ka', b'cFNqM0th'),
    (b'ADr86 ', b'QURyODYg'),
    (b'p^.k!s', b'cF4uayFz'),
])
def test__encode__with_bytes_multiple_of_3(bytes_input, expected):
    transform_test(b64.encode, bytes_input, expected)

@pytest.mark.parametrize("bytes_input,expected", [
    (b'pSj3K', b'cFNqM0s='),
    (b'ADr8 ', b'QURyOCA='),
    (b'p^.k!', b'cF4uayE='),
])
def test__encode__1_padding(bytes_input, expected):
    transform_test(b64.encode, bytes_input, expected)

@pytest.mark.parametrize("bytes_input,expected", [
    (b'pSjK', b'cFNqSw=='),
    (b'AD r', b'QUQgcg=='),
    (b'p^.}', b'cF4ufQ=='),
])
def test__encode__2_paddings(bytes_input, expected):
    transform_test(b64.encode, bytes_input, expected)

@pytest.mark.parametrize("b64_input,expected", [
    (b'MTIz', b'123'),
    (b'N1pn', b'7Zg'),
    (b'QXpV', b'AzU'),
])
def test__decode__with_input_of_lenght_4(b64_input, expected):
    transform_test(b64.decode, b64_input, expected)

@pytest.mark.parametrize("b64_input,expected", [
    (b'cFNqM0th', b'pSj3Ka'),
    (b'QURyODYg', b'ADr86 '),
    (b'cF4uayFz', b'p^.k!s'),
])
def test__decode__without_padding(b64_input, expected):
    transform_test(b64.decode, b64_input, expected)

@pytest.mark.parametrize("b64_input,expected", [
    (b'cFNqM0s=', b'pSj3K'),
    (b'QURyOCA=', b'ADr8 '),
    (b'cF4uayE=', b'p^.k!'),
])
def test__decode__with_1_padding(b64_input, expected):
    transform_test(b64.decode, b64_input, expected)

@pytest.mark.parametrize("b64_input,expected", [
    (b'cFNqSw==', b'pSjK'),
    (b'QUQgcg==', b'AD r'),
    (b'cF4ufQ==', b'p^.}'),
])
def test__decode__with_2_padding(b64_input, expected):
    transform_test(b64.decode, b64_input, expected)
