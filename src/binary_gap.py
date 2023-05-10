def solution(N):

    # # convert N to binary representation
    # binary = bin(N)[2:]

    # maximum_gap = 0
    # current_gap = 0

    # # iterate over binary digits
    # for number in binary:
    #     if number == '0':
    #         current_gap += 1

    #     else:  # update max binary gap and reset current binary gap
    #         maximum_gap = max(maximum_gap, current_gap)
    #         current_gap = 0

    # return maximum_gap
    binary = bin(N)[2:]  # Convert N to binary and remove prefix
    max_gap = 0
    current_gap = 0
    for char in binary:
        if char == '0':
            current_gap += 1
        else:
            if current_gap > 0:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
    return max_gap
