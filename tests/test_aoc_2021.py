from aoc_2021 import __version__, training


def test_version():
    assert __version__ == '0.1.0'

def test_two_numbers_add_to_2020():
    assert training.two_numbers_sum_to_2020([0, 2020]) == (0, 2020)
    assert training.two_numbers_sum_to_2020([1721, 979, 366, 299, 675, 1456]) == (1721, 299)