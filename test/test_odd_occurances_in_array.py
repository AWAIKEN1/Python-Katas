from src.odd_occurances_in_array import solution


def test_solution():
    assert solution([3, 6, 9, 6, 9]) == 5


def test_solution():
    assert solution([5, 7, 7, 5, 9]) == 9


def test_solution():
    assert solution([3, 6, 9, 6, 9, 5]) == 3, 5
