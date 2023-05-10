from src.frogJmp import solution


def test_find_num_of_jumps_when_X_less_than_Y():
    assert (solution(10, 85, 30)) == 3


def test_find_num_of_jumps_when_Y_less_than_X():
    assert (solution(50, 40, 30)) == 0


def test_find_num_of_jumps_when_X_less_than_Y_for_large_int():
    assert (solution(10000, 12000, 30)) == 67


def test_find_num_of_jumps_when_X_less_than_Y_for_very_large_int():
    assert (solution(1000000, 1200000, 40)) == 5000
