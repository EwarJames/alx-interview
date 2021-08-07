#!/usr/bin/env python3
"""You have n numbers of lock boxes in ftont you.
Each box is sequentially numbered from 0 to n-1 and
Each box might contain keys to other boxes"""


def canUnlockAll(boxes):
    """"Determines if all the boxes can be opened"""
    if not boxes:
        return False
    if type(boxes) not list:
        return False

    un_locked = [0]
    for i in un_locked:
        for key in boxes[n]:
            if key not in un_locked and boxes < len(boxes):
                un_locked.append(key)
    if len(un_locked) == len(boxes):
        return True
    return False
