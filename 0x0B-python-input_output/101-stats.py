#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""


def print_stats(size, status_codes):
    """
    function that print accumulated metrics
    """

    print("File size: {}".format(size))
    for elem in sorted(status_codes):
        print("{}: {}".format(elem, status_codes[elem]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for lin in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            lin = lin.split()

            try:
                size += int(lin[-1])
            except (IndexError, ValueError):
                pass

            try:
                if lin[-2] in valid_codes:
                    if status_codes.get(lin[-2], -1) == -1:
                        status_codes[lin[-2]] = 1
                    else:
                        status_codes[lin[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
