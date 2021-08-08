#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys


if __name__ == "__main__":
    f_size, count = 0, 1
    s = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "405": 0, "500": 0}

    def get_line(line):
        """Parse and get data"""
        try:
            p_line = line.split()
            s_code = p_line[-2]
            if s_code in s.keys():
                s[s_code] += 1
            return int(p_line[-1])
        except Exception:
            return 0

    def print_stats():
        print("File size: {}".format(f_size))
        for k in sorted(s.items()):
            if s[k]:
                print("{}: {}".format(k, s[k]))

    try:
        for line in sys.stdin:
            f_size += get_line(line)
            if count % 10 == 0:
                print_stats()
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
