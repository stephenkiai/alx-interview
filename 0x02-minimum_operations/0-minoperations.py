#!/usr/bin/python3
"""
This script calculates the fewest number of operations needed to achieve
exactly n H characters in a text file using the Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed
    to achieve exactly n H characters.
    """
    if n <= 1:
        return 0

    # Initialize array to store minimum number of operations for each index
    min_ops = [float('inf')] * (n + 1)

    min_ops[1] = 0

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Try all factors of i & update minimum number of operations
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)
                min_ops[i] = min(min_ops[i], min_ops[i // j] + j)

        # If i is a prime number, update minimum number of operations
        if min_ops[i] == float('inf'):
            min_ops[i] = i

    return min_ops[n]
