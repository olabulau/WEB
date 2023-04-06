import pytest
from yandex_testing_lesson import Rectangle


def test_wrong_type():
    with pytest.raises(TypeError):
        r = Rectangle(None, '42')


def test_wrong_values():
    with pytest.raises(ValueError):
        r = Rectangle(-1, -1)


def test_zero_wild_area():
    r = Rectangle(1, 0)
    assert r.get_area() == 0


def test_zero_height_area():
    r = Rectangle(0, 1)
    assert r.get_area() == 0


def test_zero_wild_perimetr():
    r = Rectangle(1, 0)
    assert r.get_perimeter() == 2


def test_zero_heigt_perimetr():
    r = Rectangle(0, 1)
    assert r.get_perimeter() == 2


def test_area():
    r = Rectangle(2, 3)
    assert r.get_area() == 6


def test_perimetr():
    r = Rectangle(2, 3)
    assert r.get_area() == 10