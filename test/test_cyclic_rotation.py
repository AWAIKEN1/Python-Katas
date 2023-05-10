from src.cyclic_rotation import solution


# # def test_check_there_is_an_array():
# #     a = [3, 8, 9]
# #     assert a == [3, 8, 9, 10]


def test_check_shift_element_to_right_by_one_index():
    a = [1, 2, 3, 4, 5]
    k = 1
    expected_output = [5, 1, 2, 3, 4]
    actual_output = solution(a, k)
    assert actual_output == expected_output


def test_check_if_last_element_goes_to_1st_index_when_k_is_0():
    a = [1, 2, 3, 4, 5]
    k = 2
    expected_output = [4, 5, 1, 2, 3, ]
    actual_output = solution(a, k)
    assert actual_output == expected_output


def test_check_if_shifts_3_times_when_k_is_3():
    a = [3, 8, 9, 7, 6]
    k = 3
    expected_output = [9, 7, 6, 3, 8]
    actual_output = solution(a, k)
    assert actual_output == expected_output
