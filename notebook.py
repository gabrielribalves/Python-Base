#!/usr/bin/env python
"""Notebook
$ notebook.py write --tag=tech 
Text: Anotação muito legal pessoalll

$ notebook.py read --tag=tech 

"""
__version__ = "0.1.0"

import sys
import os

arguments = sys.argv[1:]

operation, tag = arguments
tag = tag.split("=")[1]

path = os.curdir
filePath = os.path.join(path, "notes.txt")

def readNote(tag, filePath):
    for line in open(filePath):
        if line.split(":")[0] == tag:
            for phrase in line.split(",")[1:]:
                print(phrase)
            sys.exit(0)
    
    #tec:Eaeee legal hein
    # nossaaa ahhhh


def writeNote(tag, filePath):
    inputText = input("Text: ")

    with open(filePath, "a") as file_ :
        file_.write(f"Tag: {tag}\nText: {inputText}\n")


if operation == "read":
    readNote(tag, filePath)
else:
    writeNote(tag, filePath)