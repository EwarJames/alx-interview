#!/usr/bin/env python3
"""Reads stdin line by line and computes metrics"""
import sys


if __name__ = "__main__":
    f_size, count = 0, 0
    s_codes = ["200", "301", "400", "401", "403", "405", "500"]
    status = [i: 0 for i in s_codes]

    def print_status(status: dict, f_size: int) -> None:
        print("file size: {:d}".format(f_size))
        for k, v in sorted(status.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                s_code = data[-2]
                if s_code in status:
                    status[s_code] += 1
            except BaseException:
                pass
            try:
                f_size += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_status(status, f_size)
        except KeyboardInterrupt:
            print_status(status, f_size)
            raise
