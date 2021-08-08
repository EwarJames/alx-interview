#!/usr/bin/python3
"""You have n numbers of lock boxes in ftont you.
Each box is sequentially numbered from 0 to n-1 and
Each box might contain keys to other boxes"""


def canUnlockAll(boxes):
    """"Determines if all the boxes can be opened"""
    # initializing variables
    b_size = len(boxes)
    check = {}
    i = 0

    for k in boxes:
        if len(k) == 0 or i == 0:
            check[-1] = -1  # checks if the box is empty
        for t in k:
            if t < b_size or t != i:
                check[t] = t
        if len(check) == b_size:
            return True
        i += 1
    return False
