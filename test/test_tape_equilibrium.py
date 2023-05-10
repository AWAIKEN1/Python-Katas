from src.tape_equilibrium import solution


def test_check_with_small_array_N():
    input = [3, 1, 2, 4, 3]
    expected_output = 1
    assert solution(input) == expected_output


def test_check_with_large_array_of_small_numbers():
    input = [3, 1, 2, 4, 3, 6, 7, 8, 9, 10]
    expected_output = 1
    assert solution(input) == expected_output


def test_check_with_small_array_large_numbers():
    input = [300, 1000, 200, 4000, 300]
    expected_output = 2800
    assert solution(input) == expected_output


def test_check_with_large_array_large_numbers():
    input = [300, 1000, 200, 4000, 3000, 400, 5000, 6000]
    expected_output = 2100
    assert solution(input) == expected_output
