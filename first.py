#!/usr/bin/python
"""Hello World multi language

The "Hello World" change by the user's language.

Usage:
The environment variable LANG need to be configured:
    export LANG=pt-BR

Execution:

    python3 first.py
    or
    ./first.py
"""
#source .venv/bin/activate
__version__ = "0.0.1"
__author__ = "Gabrier"
__license__ = "Unlicense"

import os
import sys
os.mkn
# print(f"{sys.argv=}")

arguments = {
    "lang": None, 
    "count": 1
}


for arg in sys.argv[1:]:
    #TODO: Tratar value error
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print("invalid argument: ", key)
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    #TODO: Usar repedição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "pt_BR": "Eae mundo",
    "it_IT": "Ciao, Mondo",
    "en_US": "Hello, world",
}

print(msg[current_language] * int(arguments["count"]))