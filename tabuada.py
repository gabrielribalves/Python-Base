#!/usr/bin/env python
"""Imprime uma tabuada"""
__version__ = "0.1.1"
__author__ = "Gabrier"
__license__ = "Unlicense"

numbers = list(range(1,11))

for number in numbers:
    textTable = f"Tabuada do: {number}"
    print("{:-^30}".format(textTable))
    for table in numbers:
        result = table * number;
        textResult = f"{table} x {number} = {result}"
        print("{: ^30}".format(textResult))
    print("#" * 30)
