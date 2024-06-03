#!/usr/bin/python3
"""pascal trangle"""


def pascal_triangle(n):
    """pascal triangle"""
    father = []
    child = []
    temp = []
    if n <= 0:
        return []
    else:
        for i in range(1, n+1):
            _len = len(temp)
            child = [1]
            if i >= 3:
                for j in range(_len - 1):
                    num = temp[j] + temp[j + 1]
                    child.append(num)
            if i >= 2:
                child.append(1)
            father.append(child)
            temp = child[:]
        return father
