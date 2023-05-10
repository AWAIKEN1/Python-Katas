from src.binary_gap import solution


def test_solution():
    assert solution(9) == 2
    assert solution(529) == 4
    assert solution(20) == 1
    assert solution(15) == 0
    assert solution(32) == 0
    assert solution(1041) == 5
