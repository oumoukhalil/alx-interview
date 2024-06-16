#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    """
    minimum operation
    int (n)
    return : number of operation
    """
    nbr_opp = 0
    copy_all = 0
    past = 0
    hashtag = ['#']
    if n > 1:
        copy_all = 1
        past = 1
        hashtag.append('#')
        for i in range(n):
            _len = len(hashtag)
            if _len < n - i:
                x = _len - n
                if x % 2 == 0:
                    copy_all += 1
                    past += 1
                    hashtag.append('#')
                elif x % 2 != 0:
                    past += 1
                    hashtag.append('#')
                nbr_opp = copy_all + past
            else:
                break
    return nbr_opp
