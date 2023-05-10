from src.perm_missing_elem import solution


def test_to_check_function_works_for_empty_array():

    expected_output = 1
    actual_input = []
    assert (solution(actual_input)) == expected_output


def test_to_check_function_works_for_small_aount_of_N():

    expected_output = 4
    actual_input = [2, 3, 1, 5]
    assert (solution(actual_input)) == expected_output


def test_to_check_function_works_for_large_amount_of_N():

    expected_output = -1085
    actual_input = [200, 300, 100, 500]
    assert (solution(actual_input)) == expected_output


def test_to_check_function_works_for_very_large_amount_of_N():

    expected_output = -10985
    actual_input = [2000, 3000, 1000, 5000]
    assert (solution(actual_input)) == expected_output
