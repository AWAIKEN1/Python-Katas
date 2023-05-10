from src.frog_river_one import solution


def test_check_for_small_N_in_array():
    seconds = 7
    X = 6
    A = [1, 3, 1, 4, 2, 3, 5, 6, 4]
    assert solution(X, A) == seconds


def test_check_for_large_N_in_array():
    seconds = -1
    X = 200
    A = [10000, 30000, 10000, 4000, 20000, 30000, 50000, 60000, 40000]
    assert solution(X, A) == seconds


def test_check_for_many_N_in_array():
    seconds = 7
    X = 6
    A = [1, 3, 1, 4, 2, 3, 5, 6, 4, 3, 5, 6, 8, 9, 10]
    assert solution(X, A) == seconds
