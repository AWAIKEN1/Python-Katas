def solution(A):
    counts = {}
    for num in A:

        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

    for num in counts:
        if counts[num] % 2 == 1:
            return num


# A = [9, 3, 9, 3, 9, 7, 9]

# counts = {}  # Empty dictionary

# # First iteration: num = 9
# num = 9
# counts = {9: 1}

# # Second iteration: num = 3
# num = 3
# counts = {9: 1, 3: 1}

# # Third iteration: num = 9
# num = 9
# counts = {9: 2, 3: 1}

# # Fourth iteration: num = 3
# num = 3
# counts = {9: 2, 3: 2}

# # Fifth iteration: num = 9
# num = 9
# counts = {9: 3, 3: 2}

# # Sixth iteration: num = 7
# num = 7
# counts = {9: 3, 3: 2, 7: 1}

# # Seventh iteration: num = 9
# num = 9
# counts = {9: 4, 3: 2, 7: 1}

# # Final dictionary: counts = {9: 4, 3: 2, 7: 1}
# After the loop completes, we iterate over the dictionary to find the number with an odd count. In this case, the number 7 has an odd count of 1, so the function returns 7.
