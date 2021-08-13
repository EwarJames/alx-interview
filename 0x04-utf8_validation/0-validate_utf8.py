#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represent valid utf8 encoding"""
    # checks if the most significanr byte is 1
    m_sig = 1 << 7
    # checks if second most significant byte is 0
    sm_sig = 1 << 6
    # Tracking the number of ones occurring before zeroes
    n_sig = 0

    if not data or len(data) == 0:
        return True

    for i in data:
        sig = 1 << 7
        if n_sig == 0:
            while (i & sig):
                n_sig += 1
                i = i << 1

            if n_sig == 0:
                continue
            if n_sig == 1 or n_sig > 4:
                return False
        else:
            if not (m_sig & i and not (sm_sig & i)):
                return False
        n_sig -= 1

    if n_sig:
        return False
    return True
