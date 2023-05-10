def solution(X, A):
    leaves = {}

    for second in range(0, len(A)):
        leaves[A[second]] = True
        condition = len(leaves)
        if condition == X:
            return second
    return -1
