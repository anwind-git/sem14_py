import pytest
from myfunction import bubble_sort


def test_1():
    assert bubble_sort([5, 3, 1]) == [1, 3, 5]


def test_2():
    assert bubble_sort([150, 100, 50]) == [50, 100, 150]


def test_3():
    assert bubble_sort([35, 25, 15]) == [15, 25, 35]


if __name__ == '__main__':
    pytest.main(['-v'])