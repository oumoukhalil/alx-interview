#!/usr/bin/python3
"""UTF-8 Validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """check valid utf8

    Args
    data: List of int

    Return
    bool
    """
    remain_bytes = 0
    for byte in data:
        mask = 1 << 7
        if remain_bytes == 0:
            while byte & mask:
                remain_bytes += 1
                mask >>= 1
            if remain_bytes in (1, 7):
                return False
            elif remain_bytes == 0:
                continue

        else:
            if not (byte & (1 << 7) and not byte & (1 << 6)):
                return False

        remain_bytes -= 1
    return remain_bytes == 0
