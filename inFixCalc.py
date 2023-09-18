#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
import sys
import os
from pathlib import Path
from datetime import datetime
arguments = sys.argv[1:]

resultado = ""
validOperations = ("sum", "sub", "mul", "div")
operationDict = {
    "sum": "+",
    "sub": "-",
    "mul": "*",
    "div": "/",
}

if not arguments:
    operation = input("Operation: ")
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("The arguments are wrong")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, * nums = arguments

if operation not in validOperations:
    print("Invalid operation")
    print(validOperations)
    sys.exit(2)

validNums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Invalid number {num}")
        sys.exit(3)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validNums.append(num)

n1, n2 = validNums

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

resultText = "O resultado é: " + str(result)

path = os.curdir
filePath = os.path.join(path, "infixCalc.log")
timeStamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

file_ = open(filePath, "a")
file_.write(f"{timeStamp} | {user} | {n1} {operationDict[operation]} {n2} = {result}\n")
file_.close()

print(resultText)