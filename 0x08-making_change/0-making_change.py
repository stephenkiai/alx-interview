#!/usr/bin/python3
"""fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """make changes"""
    tmp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            tmp_value += total // coin
            total = total % coin

    return tmp_value if total == 0 else -1


if __name__ == '__main__':

    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
