#!/usr/bin/env python
"""Notebook"""

import sys

try:
    names= open("names.txt").readlines()
    1 / 1
    print(names.banana)
except FileNotFoundError:
    print("[Error] FileNotFoundError")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] ZeroDivisionError")
    sys.exit(1)
except AttributeError as e:
    print(str(e))
    sys.exit(1)
else:
    print("Success")
finally:
    print("Always execute")

try:
    print(names[2])
except:
    print("[Error] 2")
    sys.exit(1)