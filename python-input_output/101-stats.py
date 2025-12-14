#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys


def print_stats(total_size, status_counts):
    """Prints the collected statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    valid_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                status = parts[-2]
                if status in valid_codes:
                    status_counts[status] = status_counts.get(status, 0) + 1
            except IndexError:
                pass
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
    print_stats(total_size, status_counts)
