#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as tr:
        print(f"Exception: {tr}", file=sys.stderr)
        return False
