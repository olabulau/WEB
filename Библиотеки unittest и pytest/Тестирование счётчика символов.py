import pytest
from yandex_testing_lesson import count_chars


def test_empty():
    count = count_chars('')
    assert count == {}


def test_wrong_type():
    with pytest.raises(TypeError):
        count_chars(42)


def test_common():
    count = count_chars('aabccc')
    assert count == {'a': 2, 'b': 1, 'c': 3}