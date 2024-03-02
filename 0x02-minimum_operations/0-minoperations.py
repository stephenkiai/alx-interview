#!/usr/bin/python3
"""
This script calculates the fewest number of operations needed to achieve
exactly n H characters in a text file using the Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculate minimum number of operations needed to get `n` 'H' characters.

    Returns:
    int: minimum number of operations needed to get `n` 'H' characters. If `n`
         is impossible to achieve, return 0.
    """
    nH = 0
    x = 2
    while n > 1:
        while n % x == 0:
            nH += x
            n /= x
        x += 1
    return nH
