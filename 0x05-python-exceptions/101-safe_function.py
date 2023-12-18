#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(args)
    except Exception as tr:
        print(f"Exception: {tr}", file=sys.stderr)
        return None
