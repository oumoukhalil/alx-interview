#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """lockboxes
    boxes: list of lists
    return: True or False
    """
    n = len(boxes)
    for i in range(1, n-1):
        if (len(boxes[i]) == 0):
            return False
    return True
