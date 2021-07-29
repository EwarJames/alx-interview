#!/usr/bin/python3
"""
Minimum operations
"""



def minOperations(n):
    """
    In a text file there is a single character H.
    Your text editor can execute two operations in this file:
    Copy All and Paste. Given a number n, Write a method that calculates
    the fewest numbber of operations needed to result in exactly n H
    characters in the files
    """
    if n <= 1:
        return 0
    t, d, p = n, 2, 0

    while t > 1:
        if t % d == 0:
            t = t / d
            p = p + d
        else:
            d = d + 1
    return p
