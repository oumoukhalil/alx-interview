#!/usr/bin/python3

def makeChange(coins, total):
    """make change

    Arguments
    ---------
    coints: list of int or float
    total: int or float

    Return
    ------
    int
    """
    sum = 0
    _len = len(coins)
    if total <= 0:
        return 0
    else:
        for i in coins:
            sum += i
        if sum > total:
            return (-1)
        else:
            return (_len)
