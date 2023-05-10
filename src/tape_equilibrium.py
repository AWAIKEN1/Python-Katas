def solution(A):
    left_sum = A[0]
    right_sum = sum(A[1:])
    min_diff = abs(left_sum - right_sum)
    for i in range(1, len(A) - 1):
        left_sum += A[i]
        right_sum -= A[i]
        diff = abs(left_sum - right_sum)
        if diff < min_diff:
            min_diff = diff
    return min_diff

    # A non-empty array A consisting of N integers is given

    # Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

    # The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

    # In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

    # For example, consider array A such that:

    #   A[0] = 3
    #   A[1] = 1
    #   A[2] = 2
    #   A[3] = 4
    #   A[4] = 3
    # We can split this tape in four places: [3,1,2,4,3]

    # P = 1, difference = |3 − 10| = 7
    # P = 2, difference = |4 − 9| = 5
    # P = 3, difference = |6 − 7| = 1
    # P = 4, difference = |10 − 3| = 7
    # Write a function:

    # def solution(A)

    # that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

    # For example, given:

    #   A[0] = 3
    #   A[1] = 1
    #   A[2] = 2
    #   A[3] = 4
    #   A[4] = 3
    # the function should return 1, as explained above.

    # Write an efficient algorithm for the following assumptions:

    # N is an integer within the range [2..100,000];
    # each element of array A is an integer within the range [−1,000..1,000].


# The algorithm initializes the left_sum variable to be the first element of the array and the right_sum variable to be the sum of the remaining elements of the array. It then calculates the absolute difference between these two sums and sets it as the initial value of min_diff.

# It then iterates over all possible split points(from index 1 to index N-2), calculating the new left_sum and right_sum values for each split point and the absolute difference between them. If the difference is smaller than the current value of min_diff, it updates min_diff to be the new difference.

# Finally, it returns the minimum difference that was found.

# As an example, consider the input array A = [3, 1, 2, 4, 3]. The algorithm would first calculate left_sum = 3 and right_sum = 10, and set min_diff to be abs(3 - 10) = 7. It would then calculate the absolute differences for each split point as follows:

# For P = 1: left_sum = 3, right_sum = 9, diff = abs(3 - 9) = 6
# For P = 2: left_sum = 4, right_sum = 8, diff = abs(4 - 8) = 4
# For P = 3: left_sum = 6, right_sum = 7, diff = abs(6 - 7) = 1
# For P = 4: left_sum = 10, right_sum = 3, diff = abs(10 - 3) = 7
# The minimal difference that can be achieved is 1, which is returned by the algorithm.
